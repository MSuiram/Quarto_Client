import socket
import sys
import json
import time
import threading

class aclient():
    def __init__(self, IP = socket.gethostname(), port = int(sys.argv[1])):
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
        print(f"ClientRecv {respons}")
        return(respons)
            
    def subscribe(self):
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
                print(respons)
                finished = True
            except IndentationError:
                pass

    def pong(self,c):
        c.send(json.dumps({"response": "pong"}).encode())
        print(f"ClientSend pong")
    
    def run(self):
        self.subscribe()
        while True:
            self.s2.listen()
            c ,addr = self.s2.accept()
            request = self.receive(c)
            if request["request"] == "ping":
                self.pong(c)
                



aclient().run()



