import random
import time

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

class algoritm():
    def __init__(self, board = [], piece = None):
        self.board = board
        self.piece = piece
        self.lines = [
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

    def timeit(fun):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = fun(*args, **kwargs)
            print(f"Executed in {time.time()-start}")
            return res
        return wrapper

    def life(self):
        print(self.data["lives"])
        print(self.data["errors"])

    def states(self):
        self.board = self.data["state"]["board"]
        self.piece = self.data["state"]["piece"]
    
    @timeit
    def winner(self):
        for line in self.lines:
            values = list((self.board[i] for i in line))
            for i in range(len(values)):
                if values[i] != None:
                    values[i] = set(values[i])
            print(values)
            intersection1 = intersection(values[0],values[1])
            intersection2 = intersection(values[2],values[3])
            inter = intersection(intersection1,intersection2)
            print(inter)
            
            if None not in values and len(inter) == 1:
                return 1
        return None
        
    def choice_pos(self):
        poss = []
        for i in range(len(self.board)):
            if self.board[i] == None:
                poss.append(i)
        return random.choice(poss)

    def choice_piece(self):
        liste = [set("BDEC"),set("BDEP"),set("BDFC"),set("BDFP"),set("BLEC"),set("BLFC"),set("BLEP"),set("BLFP"),set("SDEC"),set("SDEP"),set("SDFC"),set("SDFP"),set("SLEC"),set("SLFC"),set("SLEP"),set("SLFP")]
        if self.piece != None:
            liste.remove(set(self.piece))
        for i in self.board:
            if i != None:
                liste.remove(set(i))
            else:
                pass
        print(liste)
        if liste != []:
            return "".join(random.choice(liste))
        else:
            return None
        
    @timeit
    def run(self, data):
        self.data = data
        self.life()
        self.states()
        return({"pos": self.choice_pos(),
                "piece": self.choice_piece()
                })
print(algoritm([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP").winner())