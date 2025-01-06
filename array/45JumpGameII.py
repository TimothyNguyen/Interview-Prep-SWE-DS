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
        ans = [float('inf')]*len(nums)
        ans[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                ans[i] = 1
            elif nums[i] > 0:
                val = i + 1
                v = min(ans[val:i+nums[i]+1])
                if v != float('inf'):
                    ans[i] = int(v) + 1
        return ans[0]

        '''
        jumps = 0
            current_jump_end = 0
            farthest = 0
            for i in range(len(nums) - 1):
                # we continuously find the how far we can reach in the current jump
                farthest = max(farthest, i + nums[i])
                # if we have come to the end of the current jump,
                # we need to make another jump
                if i == current_jump_end:
                    jumps += 1
                    current_jump_end = farthest
            return jumps
        '''
            
            
    
'''
[2, 3, 1, 1, 4]
[2, 1, 2, 1, 0]


[2, 3, 0, 1, 4]
[2, 1, inf, 1, 0]
'''