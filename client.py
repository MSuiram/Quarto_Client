import socket
import sys
import json
import time

class client():
    def __init__(self, IP = socket.gethostname(), port = int(sys.argv[1])):
        self.s = socket.socket()
        self.s.connect((IP, port))

    def subscribe(self):
        order = json.dumps({"request": "subscribe",
                            "port": 5000,
                            "name": "SuiraBot",
                            "matricules": ["23004"]
                            }).encode()
        sent = self.s.send(order)
        if sent == len(order):
            print("OK")
    
    def pong(self):
        pass
    
    def run(self):
        self.subscribe()
        while True:
            time.sleep(1)

client().run()



