import socket
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
        self.pos = self.connect()
        #print(getActionsCounter(), self.id)

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        
        except socket.error as e:
            print(e)

# Testing
# n = Network()
# print(getActionsCounter(), n.send("hello"))
# print(getActionsCounter(), n.send("working"))
