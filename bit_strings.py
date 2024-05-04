def string_to_bits(string):
    return ''.join(format(ord(c), '08b') for c in string)


def bits_to_string(bits):
    # Split the bit string into 8-bit chunks
    chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]
    
    # Convert each 8-bit chunk into its corresponding ASCII character
    chars = [chr(int(chunk, 2)) for chunk in chunks]
    
    # Concatenate all the characters to form the resulting string
    return ''.join(chars)