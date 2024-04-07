import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',6655))

while True:
    data_size=input("Enter Data SIZE : ")
    s.send(data_size.encode())    
    no_of_routers=input("Enter Number of Routers Present in the path ")
    s.send(no_of_routers.encode())
    for x in range(int(no_of_routers)):
        s.send(input(f"Enter MTU of Router{x+1}").encode())
    s.close()
    break
    