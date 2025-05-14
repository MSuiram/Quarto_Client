import socket
import sys
import json
import algo
import random

# Ne pas oublier de désactiver le pare feu (Celui de Avast)

class client():
    def __init__(self, IP = str(sys.argv[1]), port = int(sys.argv[2])):
        self.s1 = socket.socket()
        self.s1.connect((IP, port))
        self.s2 = socket.socket()
        self.s2.bind((socket.gethostname(), 5000))
        

    def receive(self,c):
        finished = False
        chunks =[]
        while not finished:
            data = c.recv(1024)
            chunks.append(data)
            try:
                respons = json.loads(b"".join(chunks).decode())
                finished = True
            except IndentationError:
                pass
        print(f"[Message] ClientRecv {respons}")
        return(respons)
            
    def subscribe(self):
        sub = False
        while not sub:
            order = json.dumps({"request": "subscribe",
                                "port": 5000,
                                "name": "SuiraBot",
                                "matricules": ["23004"]
                                }).encode()
            self.s1.send(order)
            finished = False
            chunks =[]
            while not finished:
                data = self.s1.recv(1024)
                chunks.append(data)
                try:
                    respons = json.loads(b"".join(chunks).decode())
                    finished = True
                except IndentationError:
                    pass
            if respons["response"] == "ok":
                sub = True
            if respons["response"] == "error":
                print(f"[Error] {respons["error"]}")
        self.s1.close()

    def message(self):
        message_liste = [
            "C'est pas faux !",
            "Faut arrêter ces conneries de nord et de sud ! Une fois pour toutes, le nord, suivant comment on est tourné, ça change tout !",
            "Faut pas respirer la compote, ça fait tousser.",
            "Moi j'ai appris à lire, ben je souhaite ça à personne.",
            "La patience est un plat qui se mange sans sauce.",
            "La patience est un plat qui se prépare à l'avance.",
            "Je pense que vous glandouillez bien assez dans la réalité pour qu'on puisse se permettre d'optimiser le fictionnel.",
            "Parce qu'en fait, dans notre langue, y'a que deux mots qui riment avec complète : c'est quiquette et biseautée. Alors ça va être chaud !",
            "Et si on envoyait quelqu'un qui se faufile dans leur camp sans se faire repérer pour observer leurs faits et gestes ? Ou alors, ça fait doublon avec l'espionnage ? Je me rends pas compte …",
            "Du passé faisons table en marbre.",
            "13, 14, 15 … Enfin, tous les chiffres impairs jusqu'à 22.",
            "Là, vous faites sirop de vint-et-un et vous dites : beau sirop, mi-sirop, siroté, gagne-sirop, sirop grelot, passe-montagne, sirop au bon goût.",
            "C'est vrai que c'est curieux cette manie de pas vouloir torture; ça vient de quoi, ça ?",
            "La chevalerie, c'est pas là où on range les chevaux ?",
            "À Kadoc ! À Kadoc !",
            "Elle est où la poulette ?",
            "Quand y'a plus de roi, c'est caca.",
            "Les chiffres, c'est pas une science exacte figurez-vous !",
            "C'est compliqué mais c'est compliqué !",
            "Tempora mori, tempora mundis recorda. Voilà. Eh bien ça, par exemple, ça veut absolument rien dire, mais l'effet reste le même, et pourtant j'ai jamais foutu les pieds dans une salle de classe, attention !",
            "Sire, Sire ! On en a gros !",
            "C'qui compte, c'est les valeurs !"
        ]
        return random.choice(message_liste)

    def pong(self,c):
        c.send(json.dumps({"response": "pong"}).encode())
        print(f"[Message] ClientSend pong")
    
    def move(self,c,request):
        respons = algo.algoritm().run(request)
        c.send(json.dumps({"response": "move",
                           "move": respons,
                           "message": self.message()
                           }).encode())
        print(f"[Message] Your respons is {respons}")
        print("==========================")

    def run(self):
        self.subscribe()
        while True:
            self.s2.listen()
            c ,addr = self.s2.accept()
            request = self.receive(c)
            if request["request"] == "ping":
                self.pong(c)
            if request["request"] == "play":
                self.move(c,request)
client().run()



