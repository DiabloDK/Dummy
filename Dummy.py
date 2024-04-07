class IPv4Packet:
    def __init__(self, source, destination, payload, mtu, fragment_id=0, fragment_offset=0, total_length=0, flags=0):
        self.source = source
        self.destination = destination
        self.payload = payload
        self.mtu = mtu
        self.fragment_id = fragment_id
        self.fragment_offset = fragment_offset
        self.total_length = total_length
        self.flags = flags

    def fragment(self):
        fragments = []
        payload_len = len(self.payload)
        offset = 0
        while payload_len > 0:
            if payload_len <= self.mtu - 20:  # -20 for IP header
                fragments.append(IPv4Packet(self.source, self.destination, self.payload[offset:], self.mtu,
                                            self.fragment_id, self.fragment_offset + offset, len(self.payload),
                                            self.flags))
                break
            else:
                fragments.append(IPv4Packet(self.source, self.destination, self.payload[offset:offset+self.mtu-20], 
                                            self.mtu, self.fragment_id, self.fragment_offset + offset, 
                                            len(self.payload), self.flags | 0x2000 if offset > 0 else 0))
                payload_len -= self.mtu - 20
                offset += self.mtu - 20
        return fragments

    @staticmethod
    def reassemble(fragments):
        fragments.sort(key=lambda x: x.fragment_offset)
        data = b''
        for frag in fragments:
            data += frag.payload
        return data


class Router:
    def __init__(self, mtu):
        self.mtu = mtu

    def forward_packet(self, packet, next_hop):
        if packet.mtu <= self.mtu:
            print(f"Router forwarding packet: {packet.payload}")
            return True
        else:
            print(f"Packet too large for router. Fragmenting...")
            fragments = packet.fragment()
            for fragment in fragments:
                self.forward_packet(fragment, next_hop)
            return False


def main():
    router1 = Router(1500)
    router2 = Router(1000)

    source = "192.168.1.1"
    destination = "192.168.2.1"
    payload = b"Hello, World!"
    
    packet = IPv4Packet(source, destination, payload, 2000, fragment_id=12345)  # Create IPv4 packet with payload exceeding MTU of first router
    print("Original packet:")
    print(packet.payload.decode())

    router1.forward_packet(packet, router2)


if __name__ == "__main__":
    main()
