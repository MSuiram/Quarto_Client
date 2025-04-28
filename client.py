import socket
import sys
import json
import algo

# Ne pas oublier de désactiver le pare feu (Celui de Avast)

class client():
    def __init__(self, IP = socket.gethostname(), port = int(sys.argv[1])):
        self.port = port
        self.s1 = socket.socket()
        self.s1.connect((IP, 3000))
        self.s2 = socket.socket()
        self.s2.bind((socket.gethostname(), self.port))
        

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
        print(f"ClientRecv {respons}")
        return(respons)
            
    def subscribe(self):
        sub = False
        while not sub:
            order = json.dumps({"request": "subscribe",
                                "port": self.port,
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
                print(f"ERROR: {respons["error"]}")
        self.s1.close()

    def pong(self,c):
        c.send(json.dumps({"response": "pong"}).encode())
        print(f"ClientSend pong")
    
    def move(self,c,request):
        respons = algo.algoritm().run(request)
        c.send(json.dumps({"response": "move",
                           "move": respons,
                           "message": "Fun message"
                           }).encode())
        print(respons)

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



