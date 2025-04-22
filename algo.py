import random

class algoritm():
    def __init__(self):
        self.board = []
        pass

    def life(self):
        print(self.data["lives"])
        print(self.data["errors"])

    def states(self):
        self.board = self.data["state"]["board"]
        self.piece = self.data["state"]["piece"]

    def choice_pos(self):
        poss = []
        for i in range(self.board):
            if self.board[i] == "null":
                poss.append(i)
        return random.choice(poss)

    def choice_piece(self):
        liste = [["B","S"],["D","L"],["E","F"],["C","P"]]
        a = []
        while "".join(a) == self.board:
            for i in liste:
                a.append(random.choice(i))
        return "".join(a)

    def run(self, data):
        self.data = data
        self.life()
        self.states()
        return {"pos": self.choice_pos(),
                "piece": self.choice_pos()
                }
