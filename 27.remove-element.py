#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        fast=0
        slow=0
        size=len(nums)
        while fast < size:
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow
        
        fast=0
        slow=0
        size=len(nums)
        while fast < size:
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow

        # 1 2 3 4 5    2
        # slow = 4 fast = 5
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
# @lc code=end

