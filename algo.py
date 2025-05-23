import random
import time
import ABPruning

class algoritm():
    def __init__(self, board = [], piece = None):
        self.board = board
        self.piece = piece

    def timeit(fun):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = fun(*args, **kwargs)
            print(f"[Timeit] Executed in {time.time()-start}")
            return res
        return wrapper

    def life(self):
        if self.data["errors"] == []:
            print(f"[Message] You have {self.data["lives"]} lives")
        else:
            print(f"[Error] You have {self.data["lives"]} lives and error is {self.data["errors"]}")

    def states(self):
        self.board = self.data["state"]["board"]
        self.piece = self.data["state"]["piece"]
        self.current = self.data["state"]["current"]

    def choice_pos(self):
        self.move, self.thePiece = ABPruning.next(self.board, self.piece, self.current)

    def random_choice_pos(self):
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
        if liste != []:
            return "".join(random.choice(liste))
        else:
            return None
        
    @timeit
    def run(self, data):
        self.data = data
        self.life()
        self.states()
        if self.piece == None:
            return({"pos": None,
                "piece": self.choice_piece()
                })
        self.choice_pos()
        if self.move == None:
            print("Random")
            self.move = self.random_choice_pos()
        return({"pos": self.move,
                "piece": self.thePiece
                })
