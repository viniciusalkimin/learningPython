from socket import *

server="127.0.0.1"
port="43210"

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, port))
out=""
while out!="X":
    msg=input("Type your message: ")
    obj_socket.sendTo(msg.encode(), (server, port))
    data, origin = obj_socket.recvfrom(65535)
    print("Server Response: ", data.enconde())
    out=input("Type <X> to quit:").upper()

obj_socket.close()
