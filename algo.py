import random

class algoritm():
    def __init__(self):
        self.board = []

    def life(self):
        print(self.data["lives"])
        print(self.data["errors"])

    def states(self):
        self.board = self.data["state"]["board"]
        self.piece = self.data["state"]["piece"]

    def choice_pos(self):
        poss = []
        for i in range(len(self.board)):
            if self.board[i] == None:
                poss.append(i)
        return random.choice(poss)

    def choice_piece(self):
        liste = ["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP","SLFP"]
        if self.piece != None:
            liste.remove(self.piece)
        for i in self.board:
            if i != None:
                liste.remove(i)
            else:
                pass
        print(liste)
        return random.choice(liste)

    def run(self, data):
        self.data = data
        self.life()
        self.states()
        return({"pos": self.choice_pos(),
                "piece": self.choice_piece()
                })
        
