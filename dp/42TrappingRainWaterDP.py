class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        l = [0] * len(height)
        r = [0] * len(height)
        res = 0
        
        n = len(height)
        for i in range(0, n):
            if i == 0:
                l[i] = height[i]
                r[len(height) - i - 1] = height[n - i - 1]
            else:
                l[i] = max(height[i], l[i-1])
                r[n - i - 1] = max(height[n - i - 1], r[n - i])

        for i in range(1, len(height)):
            res += min(l[i], r[i]) - height[i]

        return res

'''
left, right = 0, len(height) - 1
left_max, right_max = 0, 0
water = 0
while left < right:
    if height[left] < height[right]:
        left_max = max(left_max, height[left])
        water += max(0, left_max - height[left])
        left += 1
    else:
        right_max = max(right_max, height[right])
        water += max(0, right_max - height[right])
        right -= 1
    # print(height)
return water
'''