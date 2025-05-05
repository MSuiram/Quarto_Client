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

def intersection(a , b):
    if a is None:
        return b
    if b is None:
        return a
    inter = set()
    for val in a:
        if val in b:
            inter.add(val)
    return inter

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


def winner(state):
    for line in lines:
        values = list((state[i] for i in line))
        for i in range(len(values)):
            if values[i] != None:
                values[i] = set(values[i])
        intersection1 = intersection(values[0],values[1])
        intersection2 = intersection(values[2],values[3])
        inter = intersection(intersection1,intersection2)
        if None not in values and len(inter) == 1:
            return 1
    return None
    
def utility(state, piece):
    theWinner = winner(state)
    if theWinner is None:
        return 0
    if theWinner == piece:
        return 1
    return -1
    
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
    player = piece
    res = list(state)
    if move != None:
        res[move] = player
    return res

def lineValue(line, piece):
    piece = list(piece)
    counter = {
        piece[0] : 0,
        piece[1] : 0,
        piece[2] : 0,
        piece[3] : 0,
        None : 0
    }
    for elem in line:
        if elem != None:
            elem = list(elem)
            for type in elem:
                if type in list(counter.keys()):
                    counter[type] += 1
        counter[None] += 1
    if counter[None] + max([counter[piece[0]],counter[piece[1]],counter[piece[2]],counter[piece[3]]]) == 4:
        return 1
    return 0

def heuristic(state, piece):
    if gameOver(state):
        theWinner = winner(state)
        if theWinner is None:
            return 0
        if theWinner == piece:
            return 40
        return 0
    res = 0
    for line in lines:
        res += lineValue([state[i] for i in line], piece)
    return res

def negamaxWithPruningIterativeDeepening(state, piece, timeout = 2):
    cache = defaultdict(lambda : 0)
    def negamaxWithPruningLimitedDepth(state, piece, depth=3, alpha = float('-inf'), beta = float('inf'), start = time.time(), timeout = 0.3):
        over = gameOver(state)
        if over or depth == 0:
            res = -heuristic(state, piece), None, over, piece
        
        else:
            theValue, theMove = float('-inf'), None
            possibilities = [(move, apply(state, piece, move)) for move in moves(state)]
            possibilities.sort(key=lambda poss: cache[tuple(poss[1])])
            for move in moves(state):
                for piec in pieces_list(state, piece):
                    if time.time() - start > timeout:
                        raise NoTimeError()
                    successor = apply(state, piece, move)
                    value, _, over, thePiece = negamaxWithPruningLimitedDepth(successor, piec, depth-1, -beta, -alpha, start, timeout)
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
    while value > -40 and time.time() - start < timeout and not over:
        try:
            value, move, over, thePiece = negamaxWithPruningLimitedDepth(state, piece, depth, start=start, timeout=timeout)
            depth += 1
        except NoTimeError:
            break
    if thePiece == None:
        thePiece = random.choice(pieces_list(state, piece))
    print(f"La profondeur est de {depth}")
    return value, move, thePiece

def next(state, piece):
    _, move, thePiece =negamaxWithPruningIterativeDeepening(state, piece)
    return move, thePiece
