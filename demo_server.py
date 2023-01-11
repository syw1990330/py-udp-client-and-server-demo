import socket
import threading

# def client_recv(client,address):
#     print(address,'client address')
#     with client:
#         while True:
#             data = client.recv(1024)
#             if not data:
#                 break
#             client.sendall(data)
    
#     print(f'client address:{address} broken')


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
        

        # th_client = threading.Thread(target=client_recv,args=[client,address])
        # th_client.start()
            





            