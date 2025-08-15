import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),9999))
s.listen(3)
while True:
    client,addr=s.accept()
    print(f'connected with the client {addr}')
    client.send(bytes("i am sending msg","uft-8"))
    client.close()