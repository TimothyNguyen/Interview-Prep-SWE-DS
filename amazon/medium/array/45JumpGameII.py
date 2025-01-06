'''
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a 
forward jump from index i. In other words, if you are 
at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach 
nums[n - 1].

Input: nums = [2,3,1,1,4]
Output: 2

Input: nums = [2,3,0,1,4]
Output: 2
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf') for _ in range(len(nums))]
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                dp[i] = 1
            elif nums[i] > 0:
                min_val = min(dp[i+1:nums[i] + i + 1])
                if min_val != float('inf'):
                    dp[i] = min_val + 1
        return dp[0]
