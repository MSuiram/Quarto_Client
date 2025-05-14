import random
from collections import defaultdict
import time

class NoTimeError(Exception):
    pass

lines = [
                    [0,1,2,3],
                    [4,5,6,7],
                    [8,9,10,11],
                    [12,13,14,15],
                    [0,4,8,12],
                    [1,5,9,13],
                    [2,6,10,14],
                    [3,7,11,15],
                    [0,5,10,15],
                    [3,6,9,12]
                    ]

def pieces_list(state, piece):
    pieces = ["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP","SLFP"]
    for i in range(len(pieces)):
        pieces[i] = set(pieces[i])

    pieces.remove(set(piece))
    for i in range(len(state)):
        if state[i] != None:
            if set(state[i]) in pieces:
                pieces.remove(set(state[i]))

    for i in range(len(pieces)):
        pieces[i] = "".join(pieces[i])
    return pieces

def align(state, piece):
    for line in lines:
        counter = {None : 0}
        pos_none = None
        inter = {"B","S","D","L","E","F","C","P"}
        for i in line:
            if state[i] == None:
                counter[None] += 1
                pos_none = i
            if state[i] != None:
                inter = inter.intersection(state[i])
        inter = inter.intersection(set(piece))
        if counter[None] == 1:
            if len(inter) == 2 or len(inter) == 1:
                return pos_none
    return None 

def winner(state): 
    for line in lines:
        values = list((state[i] for i in line))
        if None not in values:
            inter = set(values[0])
            for i in range(3):
                inter = inter.intersection(values[i+1])
            if len(inter) == 1 or len(inter) == 2:
                return 1
    return None
    
def gameOver(state):
    if winner(state) is not None:
        return True
        
    empty = 0
    for element in state:
        if element is None:
            empty += 1
    return empty == 0

def moves(state):
    res = []
    for i, element in enumerate(state):
        if element is None:
            res.append(i)
        
    random.shuffle(res)
    return res
  
def apply(state, piece, move):
    res = list(state)
    if move != None:
        res[move] = piece
    return res

def lineValue(line):
    pieces = []
    counter = {
        None : 0
    }
    for elem in line:
        if elem == None:
            counter[None] += 1
        if elem != None:
            pieces.append(set(elem))
    inter = {"B","S","D","L","E","F","C","P"}
    for i in range(len(pieces)):
        inter = inter.intersection(pieces[i])
    
    if counter[None] == 1:
        if len(inter) != 0:
            return 20 
    return len(inter) + (4-counter[None])

def heuristic(state, player):
    if gameOver(state):
        theWinner = winner(state)
        if theWinner is None:
            return 0
        if theWinner == player:
            return 400
        return -400
    res = 0
    for line in lines:
            res += lineValue([state[i] for i in line])
    return res

def negamaxWithPruningIterativeDeepening(state, piece, player, current, timeout = 2):
    cache = defaultdict(lambda : 0)
    def negamaxWithPruningLimitedDepth(state, piece, player, current, depth=3, alpha = float('-inf'), beta = float('inf'), start = time.time(), timeout = 0.3):
        over = gameOver(state)
        theOver = over
        thePiece = None
        if over or depth == 0:
            res = -heuristic(state, player), None, over, piece
        
        else:
            theValue, theMove = float('-inf'), None
            possibilities = [(move, apply(state, piece, move)) for move in moves(state)]
            possibilities.sort(key=lambda poss: cache[tuple(poss[1])])
            for move in moves(state):
                for piec in pieces_list(state, piece):
                    if time.time() - start > timeout:
                        raise NoTimeError()
                    successor = apply(state, piece, move)
                    value, _, over, thePiece = negamaxWithPruningLimitedDepth(successor, piec, (player+1)%2, current, depth-1, -beta, -alpha, start, timeout)
                    theOver = over
                    if value > theValue:
                        theValue, theMove, thePiece = value, move, piec
                    alpha = max(alpha, theValue)
                    if alpha >= beta:
                        break
            res =  -theValue, theMove, theOver, thePiece
        cache[tuple(state)] = res[0]
        return res
    
    value, move = 0, None
    depth = 1
    start = time.time()
    over = False
    thePiece = None

    if align(state, piece) != None:
        print("[Message] You are Win !!!")
        return None ,align(state, piece), None
    
    while value > -400 and time.time() - start < timeout and not over:
        try:
            value, move, over, thePiece = negamaxWithPruningLimitedDepth(state, piece, player, current, depth, start=start, timeout=timeout)
            depth += 1
        except NoTimeError:
            break
    print(f"[Message] Depth is {depth-1}")
    return value, move, thePiece

def next(state, piece, current):
    player = current
    _, move, thePiece =negamaxWithPruningIterativeDeepening(state, piece, player, current)
    return move, thePiece
