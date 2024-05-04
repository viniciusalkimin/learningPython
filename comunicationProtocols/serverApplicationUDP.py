from socket import *

server = "127.0.0.1"
port = "43210"

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server, port))
print("Server ready!")

while True:
    data, origin = obj_socket.recvfrom(65535)
    print("Origin: ", origin)
    print("Received data: ", data.decode())
    response = input("Type your response:")
    obj_socket.sendTo(response.encode(), origin)

obj_socket.close()