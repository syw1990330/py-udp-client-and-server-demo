import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_address='127.0.0.1'
port = 1234
with client_socket:
    client_socket.connect((ip_address,port))
    client_socket.send(b"this is a test")
    data,response = client_socket.recvfrom(1024)
    print(response,data.decode())
    client_socket.send(b"shutdown")
