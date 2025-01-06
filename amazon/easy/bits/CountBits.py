def count_bits(x:int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        print(x)
        print(num_bits)
        x = x >> 1
    return num_bits

# count_bits(19)
count_bits(8)

'''
10011
19 -> 9 -> 4 -> 2 -> 1
1 -> 2 -> 2 -> 2 -> 3

100
8 -> 4 -> 2 -> 1
0 -> 0 -> 0 -> 1
'''