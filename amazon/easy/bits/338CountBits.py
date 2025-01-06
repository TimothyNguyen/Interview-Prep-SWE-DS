class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = 0
        dp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] ^= i & 1
            dp[i] += (dp[i // 2])
        return dp
            