def swap_bits(n, i, j):
    print(f"Initial number: {n} (binary: {bin(n)})")

    # Extract the bits to see if they differ
    bit_i = (n >> i) & 1
    bit_j = (n >> j) & 1

    print(f"Bit at position {i}: {bit_i}, Bit at position {j}: {bit_j}")

    # If the bits are the same, no need to swap
    if bit_i == bit_j:
        print("Bits are the same; no swap needed.")
        return n
    
    # Create a bit mask to flip the bits at positions i and j
    bit_mask = (1 << i) | (1 << j)
    print(f"Bit mask for swapping: {bin(bit_mask)}")

    # XOR with the mask to flip the bits

    swapped_n = n ^ bit_mask
    print(f"Number after swapping: {swapped_n} (binary: {bin(swapped_n)})")
    
    return swapped_n

# Example usage
num = 0b101011  # Example binary number (42 in decimal)
i, j = 0, 4     # Bit positions to swap
result = swap_bits(num, i, j)