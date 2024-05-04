from socket import *

server: str = "127.0.0.1"
port = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server, port))
obj_socket.listen(2)

print("Waiting for client...")

while True:
    con, client = obj_socket.accept()
    print("Connecting with...", client)
    while True:
        received_msg = str(con.recv(1024))
        print("Receive message: ", received_msg)
        send_message = b"Hello client!"
        con.send(send_message)
        break
    con.close()
