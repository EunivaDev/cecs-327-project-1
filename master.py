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

#TESTING, may ermove
def handleNodeConnection(conn, addr):
    print(f"Node connected: {addr} and {conn}")

#TESTING, may remove
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



# from example
def pymotwMulticastExample():
    message = 'very important data'
    multicastGroup = ('224.3.29.71', 10000)

    #Create the diatagram socket
    datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set timeout so socket doesn't block indefinitely 
    datagramSocket.settimeout(0.2)


    ttl = struct.pack('b', 1)
    datagramSocket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


    try:
        print(f"sending {message}", file=sys.stderr)
        sent = datagramSocket.sendto(message.encode(), multicastGroup)

        while True:
            print("waiting to receive", file=sys.stderr)
            try:
                data, server = datagramSocket.recvfrom(16)
            except socket.timeout:
                print("timed out, no more responses", file=sys.stderr)
                break
            else:
                print(f"received {data} from {server}", file=sys.stderr)
    finally:
        print("closing socket", file=sys.stderr)
    
    







if __name__ == '__main__':
    pymotwMulticastExample()