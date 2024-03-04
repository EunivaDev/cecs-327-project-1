# Group Project 1 - A Bite of Distributed Communication
# CECS 327
# March 4, 2024
# Collaborators:
# Huy Vu - 018494734
# Kevin Tran - 029589454
# Daniel Neri - 025500083

# distSystemG17.py
# distributed system source code


# testing:
import socket
import struct
import sys
import threading

def handleNodeConnection(conn, addr):
    print(f"Node connected: {addr} and {conn}")


def startServer():
    host = "0.0.0.0"
    port = 5000

    masterSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    masterSocket.bind((host, port))
    masterSocket.listen(5)

    print(f"Master server is listening on {host}:{port}")

    while True:
        conn, addr = masterSocket.accept()
        nodeThread = threading.Thread(target=handleNodeConnection, args=(conn, addr))
        nodeThread.start()



if __name__ == '__main__':
    startServer()