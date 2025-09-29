from setup.ascii_vals_module import ascii_vals

def encode_to_base65536(text):
    """Convert text to Base65536 encoding"""
    s = text
    bit_list = [int(bit) for c in s for bit in format(ord(c), "08b")]

    output = []

    # Pad binary string to be multiple of 16
    if len(bit_list) % 16 != 0:
        for i in range(16 - (len(bit_list) % 16)):
            bit_list.insert(0, 0)

    # Extract 16-length bitstrings and reference lookup table to convert to base 2^16
    for i in range(int(len(bit_list) / 16)):
        bitstring = "".join(str(bit) for bit in bit_list[i * 16 : i * 16 + 16])
        if bitstring in ascii_vals:
            output.append(ascii_vals[bitstring])

    output = "".join(output)
    return output


# Functionality for running normally (if someone wants)
if __name__ == "__main__":
    s = "floccinaucinihilipilification"
    result = encode_to_base65536(s)
    print(result)
    with open("encode_output.py", "w", encoding="utf-8") as f:
        f.write("encode_output = " + repr(result))
