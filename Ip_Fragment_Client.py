import socket
import json


def DecryptFragments(M):
    DATA = M.decode('utf-8')
    fragmented_packets = json.loads(DATA)

    print("No of Fragments: ",len(fragmented_packets))
    for i, fragment in enumerate(fragmented_packets):
        print(f"Fragment {i+1}: {fragment}")

c = socket.socket()
c.connect(('localhost',9999))
while True:
    i = input("Please Enter the data size of the ip packet to be fragmented: ")
    c.send(i.encode())
    fragmented_packets = c.recv(1024)
    if isinstance(fragmented_packets.decode(),str) and "Error" in fragmented_packets.decode() :
        print(fragmented_packets.decode())
        continue
    else:
        DecryptFragments(fragmented_packets)
        break
