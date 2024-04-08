total_bytes= int(input("Enter the total IP datagram size (in bytes):"))
#ethernet_mtu= int(input("Enter the MTU of ethernet (in bytes):"))
#wan_mtu= int(input("Enter the MTU of WAN (in bytes):"))
ip_head_size=20
df=1
def Fragmentation(total_size,ethernet_mtu,head_size):
    num_fragments=((total_size-head_size)//(ethernet_mtu-head_size))+1
    #print("The number of fragments is: ",num_fragments)
    data=[]
    for i in range(0,num_fragments):
        df=0
        print("Fragment: ",i+1)
        if(i+1<num_fragments):
            data_size=(ethernet_mtu-head_size)
            print("The data size: ",data_size)
            offset=int(((ethernet_mtu-head_size)/8)*i)
            print("The offset is: ",offset)
            mf=1
        else:
            data_size=(total_size-head_size)-((ethernet_mtu-head_size)*i)
            print("The data size: ",data_size)
            offset=int(((ethernet_mtu-head_size)/8)*i)
            print("The offset is: ",offset)
            mf=1
        if(i+1==num_fragments):
            mf=0
            print("The MF flag is: ",mf)
        else:
            print("The MF flag is: ",mf)
        print("The DF flag is: ",df)
        data.append(data_size)
    return data

ethernet= int(input("Enter the number of ethernet:"))
wan= int(input("Enter the number of wan:"))
ether=[]
wans=[]
for i in range(0,ethernet):
    ethernet_mtu= int(input(f"Enter the MTU of ethernet {i+1} (in bytes):"))
    ether.append(ethernet_mtu)
for i in range(0,wan):
    wan_mtu= int(input(f"Enter the MTU of WAN {i+1} (in bytes):"))
    wans.append(wan_mtu)
print("The details of Ethernet fragmentation are:")
total_ether=[]
for i in ether:
    a=Fragmentation(total_bytes,i,ip_head_size)
    total_ether.append(a)
#print("The returned value is:\n",a)
#print("The value of total is:\n",total_ether)
res=0
for i in range(len(total_ether)):
    res+=len(total_ether[i])
total_wan=[]

print("The details of WAN fragmentation are:")
for i in wans:
    count=0
    for j in range(len(total_ether)):
        for k in range(len(total_ether[j])):
            print("\nThe detail: ",total_ether[j][k])
            print("The detail length: ",len(total_ether),"\n")
            b=Fragmentation(total_ether[j][k],i,ip_head_size)
            count+=1
            total_wan.append(b)
sums=0
for i in range(len(total_wan)):
    sums+=len(total_wan[i])
print("The total_fragments in wan is:",sums)
print("The total fragments in ethernet is:",res)
