import random
import time
import negamax

class algoritm():
    def __init__(self, board = [], piece = None):
        self.board = board
        self.piece = piece

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
        self.current = self.data["state"]["current"]
    
    def choice_pos(self):
        return negamax.next(self.board, self.piece)

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
