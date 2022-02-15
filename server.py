import pickle
import socket
from _thread import *
from helper import getActionsCounter
from game import Game

server = "192.168.1.229"
port = 5555

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

RED = (255,0,0)
GREEN = (0, 255,0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

s:socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(getActionsCounter(), str(e))

s.listen(2)

print(getActionsCounter(), "Waiting for connection, Server started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn: socket.socket, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))  

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game:Game = games[gameId]

                if not data:
                    print(getActionsCounter(), "Disconnected")
                    break
                else:
                    print(getActionsCounter(), "Recived: ", data)
                    if data == "reset":
                        game.resetWent()
                    elif data != "get": # Move
                        game.play(p, data)
                    
                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        
        except:
            print(getActionsCounter(), "Error in: threaded_client")
            break

    print(getActionsCounter(), "Lost connection")
    try:
        del games[gameId]
        print(getActionsCounter(), "Closing game", gameId)
    except:
        pass
    idCount -=1
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print(getActionsCounter(), "Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game[gameId]
        print(getActionsCounter(), "Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))
