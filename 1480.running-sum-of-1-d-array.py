#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[0]*len(nums)
        result[0]=nums[0]
        n=len(nums)
        for i in range(0,n):
            result[i]=nums[i]+result[i-1]
        return result
# @lc code=end

