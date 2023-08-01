#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        dp = [0]*len(nums)
        dp[0]=nums[0]
        result=dp[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            #result = max(result, dp[i])

        return max(dp)
        """
        :type nums: List[int]
        :rtype: int
        """
        
# @lc code=end

