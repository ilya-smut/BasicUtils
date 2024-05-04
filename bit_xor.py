def xor_bits(bits1, bits2):
    # Ensure both bit strings are of the same length
    if len(bits1) != len(bits2):
        raise ValueError("Bit strings must be of the same length")
    
    # Perform XOR operation bit by bit
    result = ''
    for bit1, bit2 in zip(bits1, bits2):
        result += '1' if bit1 != bit2 else '0'
    
    return result