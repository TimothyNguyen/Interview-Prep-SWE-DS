def parity(x: int) -> bool:
    '''
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits % 2 == 1
    '''
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result