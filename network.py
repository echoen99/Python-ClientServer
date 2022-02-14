import socket
import pickle
from typing_extensions import Self
from helper import getActionsCounter

server = "192.168.1.229"
port = 5555



class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        
        except socket.error as e:
            print(getActionsCounter(), e)

# Testing
# n = Network()
# print(getActionsCounter(), n.send("hello"))
# print(getActionsCounter(), n.send("working"))
