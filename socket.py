import socket
s= socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0*3000))
while True:
    packet=s.recvfrom(65565)
    print(packet)