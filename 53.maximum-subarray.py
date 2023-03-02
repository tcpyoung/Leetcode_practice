#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        m=nums[0]
        n=len(nums)
        for i in range(n):
            s=nums[i]
            for j in range(i+1,n):
                s += nums[j]
                if s>m:
                    m=s
        
        return m

        """
        :type nums: List[int]
        :rtype: int
        """
        
# @lc code=end

