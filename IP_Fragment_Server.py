import socket
import json

def convertToByte(M):
    json_data = json.dumps(M)

    # Encode the JSON string to bytes using UTF-8 encoding
    Bytes = json_data.encode('utf-8')
    return Bytes

def Fragment_IPpacket(data_size,mtu):
    if (data_size < 20):
        return  "Error: Invalid packet size."
    
    #MTU - Maximum Transmission Unit

    max_data_size = mtu - 20  # Assuming minimum IP header size is 20 bytes - 1480

        
    
    # Number of fragments needed
    num_fragments = (data_size + max_data_size - 1) // max_data_size

    print(num_fragments)
    
    fragments = []
    
    for i in range(num_fragments):
        # Calculate fragment data size
        fragment_data_size = min(data_size, max_data_size)
        
        # Set MF flag for all fragments except the last one
        if i < num_fragments - 1:
            mf_flag = 1
        else:
            mf_flag = 0
        
        # Calculate fragment offset
        fragment_offset = i * (max_data_size // 8)
        
        # Construct fragment packet
        fragment = {
            'data_size': fragment_data_size,
            'offset': fragment_offset,
            'mf_flag': mf_flag,
            'identification': 12345,  # Same for all fragments (Assumption)
            'df_flag': 0,
            'reserved_flag': 0
        }
        fragments.append(fragment)
        
        data_size -= fragment_data_size
    
    return fragments


S = socket.socket()
S.bind(('localhost', 9999))
S.listen(5)
print("Server is listening.\n")
conn,address = S.accept()
while(True):
    data = conn.recv(1024)
    if not data:
        break

    # Decode the received data
    try:
        m = int(data.decode())
    except ValueError:
        print("Error: Received data is not a valid integer")
        continue
    
    print("Received integer:", m)

    # Process the received integer
    result = Fragment_IPpacket(m,1500)
    if isinstance(result,str):
        conn.send(result.encode())
        continue
    Result = convertToByte(result)
    conn.send(Result)
