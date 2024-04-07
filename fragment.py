import math

class IPDatagramFragment:
    def __init__(self, total_length, more_fragments_bit, fragment_offset, identification, df_bit):
        self.total_length = total_length
        self.more_fragments_bit = more_fragments_bit
        self.fragment_offset = fragment_offset
        self.identification = identification
        self.df_bit = df_bit

    def construct_header(self):
        header = {
            "Identification": self.identification,
            "Total Length": self.total_length,
            "More Fragments Bit": self.more_fragments_bit,
            "Fragment Offset": self.fragment_offset,
            "DF Bit": self.df_bit,  # Do not fragment flag
            "R Bit": 0    # Reserved flag
        }
        return header

def fragment_datagram(total_data_size, mtu, identification):
    fragments = []
    num_fragments = math.ceil(total_data_size / (mtu - 20))  # MTU minus IP header size
    remaining_data = total_data_size
    offset = 0

    for i in range(num_fragments):
        fragment_size = min(remaining_data, mtu - 20)  # Maximum fragment size
        remaining_data -= fragment_size

        # Determine the More Fragments bit
        more_fragments_bit = 1 if remaining_data > 0 else 0

        # Determine the DF bit
        df_bit = 1 if remaining_data == 0 else 0

        # Construct fragment
        fragment = IPDatagramFragment(fragment_size + 20 if df_bit==0 else fragment_size, more_fragments_bit, offset, identification, df_bit)
        fragments.append(fragment)

        # Update offset for the next fragment
        offset += (fragment_size // 8)

    return fragments

def main():
    total_data_size = 5000  # Actual data size
    mtu = 1500  # Maximum Transmission Unit
    identification = 1234  # Identification number

    print("Fragmentation:")
    fragments = fragment_datagram(total_data_size, mtu, identification)
    for i, fragment in enumerate(fragments):
        print(f"Fragment {i+1}: {fragment.construct_header()}")

if __name__ == "__main__":
    main()
