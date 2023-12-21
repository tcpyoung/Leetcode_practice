#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        sDict={}
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in sDict:
                return[sDict[num2],i]
            else:
                sDict[num1]=i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
# @lc code=end

