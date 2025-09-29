from setup.ascii_vals_module import ascii_vals

def decode_from_base65536(encoded_text):
    """Convert Base65536 encoded text back to original text"""
    s = encoded_text
    list_s = list(s)

    ascii_list = []
    for i in range(len(list_s)):
        binary = [bin_str for bin_str, val in ascii_vals.items() if val == list_s[i]]
        if binary:
            binary_string = binary[0]
            first_byte = binary_string[:8]
            second_byte = binary_string[8:]

            # Convert each 8-bit chunk to ASCII character
            if int(first_byte, 2) != 0:  # Skip null padding bytes
                ascii_list.append(chr(int(first_byte, 2)))
            if int(second_byte, 2) != 0:
                ascii_list.append(chr(int(second_byte, 2)))

    full_string = "".join(ascii_list)
    return full_string


# Functionality for running from main if someone wants
if __name__ == "__main__":
    try:
        from encode_output import encode_output

        result = decode_from_base65536(encode_output)
        print(result)
    except ImportError:
        print("encode_output.py not found. Run encode.py first.")
