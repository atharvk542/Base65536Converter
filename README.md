# Base65536 Encoder

If Base64 is a bit too expressive for you, try Base65536! Every 2 ASCII characters are converted into one 16-bit unicode character. Note that many characters may be encoded into Chinese unicode characters. This is not a direct translation, however due to the organization of unicode characters, strings tend to be encoded like this. 