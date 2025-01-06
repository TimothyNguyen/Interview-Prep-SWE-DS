class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n >>= 1
            power -= 1
        return ret
'''
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
'''