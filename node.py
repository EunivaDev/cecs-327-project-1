# node.py

import socket
import struct
import sys

# temp
def connectToMaster():
    host = "master"
    port = 5000

    nodeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nodeSocket.connect((host, port))

    print(f"Connected to Master Server at {host}:{port}")


def main():
    multicastGroup = '224.3.29.71'
    serverAddress = ('224.3.29.71', 10000)
    
    datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    datagramSocket.bind(serverAddress)


    group = socket.inet_aton(multicastGroup)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    datagramSocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        print("waiting to receive message", file=sys.stderr)
        data, address = datagramSocket.recvfrom(1024)

        print(f"received {len(data)} bytes from {address}",  file=sys.stderr)

        print(data, file=sys.stderr)

        print(f'sending acknowledgement to {address}', file=sys.stderr)
        datagramSocket.sendto('ack'.encode(), address)


if __name__ == "__main__":
    main()