import random

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
    
def utility(state, player):
    theWinner = winner(state)
    if theWinner is None:
        return 0
    if theWinner == player:
        return 1
    return -1
    
def gameOver(state):
    if winner(state) is not None:
        print("a")
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
    print(res)
    return res
    
def apply(state, piece, move):
    player = piece
    res = list(state)
    res[move] = player
    return res

def heuristic(state, piece):
    if gameOver(state):
        theWinner = winner(state)
        if theWinner is None:
            return 0
        if theWinner == piece:
            return 9
        return -9
    res = 0
    for line in lines:
        res += utility([state[i] for i in line], piece)
    return res

def negamaxWithPruningLimitedDepth(state, piece, depth=4, alpha = float('-inf'), beta = float('inf')):
    if gameOver(state) or depth == 0:
        return -heuristic(state, piece), None
    
    theValue, theMove = float('-inf'), None
    for move in moves(state):
        for piec in pieces_list(state, piece):
            successor = apply(state, piece, move)
            value, _ = negamaxWithPruningLimitedDepth(successor, piec, depth-1, -beta, -alpha)
            if value > theValue:
                theValue, theMove = value, move
            alpha = max(alpha, theValue)
            if alpha >= beta:
                break
    return -theValue, theMove

def next(state, piece):
    _, move =negamaxWithPruningLimitedDepth(state, piece)
    return move