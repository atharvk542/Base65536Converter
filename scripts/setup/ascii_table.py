# Set up ASCII lookup table - not necessary to run if ascii_vals_module.py is already set up!

ascii_vals = dict()
i = 0

for codepoint in range(0x110000):
    if 0xD800 <= codepoint <= 0xDFFF:
        continue  # skip surrogates
    char = chr(codepoint)
    if char.isprintable():
        # Format to be 16 bits for base 2^16 (change if you want a different base)
        ind = format(i, "016b")
        ascii_vals[ind] = char
        i += 1

with open("ascii_vals_module.py", "w", encoding="utf-8") as f:
    f.write("ascii_vals = " + repr(ascii_vals))
