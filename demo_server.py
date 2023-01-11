import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as socket_server:
    socket_server.bind(("0.0.0.0",1234)) #0.0.0.0 represents acceptting any ip

    print("udp server is working...")
    #prevent multi-clients from causing thread blocking
    while True:
        data,address =  socket_server.recvfrom(1024)
        print(address)

        if data.decode() =="shutdown" :
            break

        print(data.decode())
        socket_server.sendto(data,address)
        

            





            
