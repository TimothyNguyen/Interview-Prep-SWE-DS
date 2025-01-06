public class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int maxans = 1;
        for (int i = 1; i < dp.length; i++) {
            int maxval = 0;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    maxval = Math.max(maxval, dp[j]);
                }
            }
            dp[i] = maxval + 1;
            maxans = Math.max(maxans, dp[i]);
        }
        return maxans;
    }
}

/*
'''
[10,9,2,5,3,7,101,18]
[1,1,1,1,1,1,1,1] r = 1
[1,1,1,1,1,1,1,1] r = 2
[1,1,1,1,1,1,1,1] r = 3
[1,1,1,2,1,1,1,1] r = 4
[1,1,1,2,2,1,1,1] r = 5
[1,1,1,2,2,3,1,1] r = 6
[1,1,1,2,2,3,4,1] r = 7
[1,1,1,2,2,3,4,4] r = 8

if dp[l] < dp[r]:
    curr_len += 1
    dp[r] = max(dp[r], curr_len)
max_ans = max(max_ans, dp[r])
'''
*/