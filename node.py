# node.py

import socket

def connectToMaster():
    host = "master"
    port = 5000

    nodeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nodeSocket.connect((host, port))

    print(f"Connected to Master Server at {host}:{port}")


if __name__ == "__main__":
    connectToMaster()