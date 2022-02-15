import pickle
import socket
from _thread import *
from helper import getActionsCounter
from player import Player

server = "192.168.1.229"
port = 5555

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

RED = (255,0,0)
GREEN = (0, 255,0)
BLUE = (0, 0, 255)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(getActionsCounter(), str(e))

s.listen(2)
print(getActionsCounter(), "Waiting for connection, Server started")

players = [Player(0,0,PLAYER_WIDTH,PLAYER_HEIGHT,RED), Player(100,100,PLAYER_WIDTH,PLAYER_HEIGHT,GREEN)]

def threaded_client(conn, player):
    #conn.send(str.encode("Connected"))    
    conn.send(pickle.dumps(players[player]))    
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            #reply = data.decode("utf-8")

            if not data:
                print(getActionsCounter(), "Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print(getActionsCounter(), "Received: ", data)
                print(getActionsCounter(), "Sending: ", reply)

                conn.sendall(pickle.dumps(reply))
        
        except:
            print(getActionsCounter(), "Error in: threaded_client")
            break

    print(getActionsCounter(), "Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print(getActionsCounter(), "Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))

    currentPlayer += 1
