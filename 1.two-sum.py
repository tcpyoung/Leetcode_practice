#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]+nums[j] == target:
                    return i,j
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
# @lc code=end

