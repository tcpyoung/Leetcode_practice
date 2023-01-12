#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        records = dict()

        for index, value in enumerate(nums):
            if target-value in records:
                return [records[target-value],index]
            records[value]=index
        return[]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
# @lc code=end

