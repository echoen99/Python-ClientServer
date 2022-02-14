import socket
from _thread import *
import sys
from helper import getActionsCounter, read_pos, make_pos

server = "192.168.1.229"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print(getActionsCounter(), "Waiting for connection, Server started")

pos = [(0,0), (100,100)]

def threaded_client(conn, player):
    #conn.send(str.encode("Connected"))    
    conn.send(str.encode(make_pos(pos[player])))    
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            #reply = data.decode("utf-8")

            if not data:
                print(getActionsCounter(), "Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print(getActionsCounter(), "Received: ", data)
                print(getActionsCounter(), "Sending: ", reply)

                conn.sendall(str.encode(make_pos(reply)))
        
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
