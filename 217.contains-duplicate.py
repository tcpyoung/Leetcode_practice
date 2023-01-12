#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        record= dict()
        for num in nums:
            if num in record.keys(): 
                return True
            else:
                record[num]=True
        
        return False
           
        """
        :type nums: List[int]
        :rtype: bool
        """
        
# @lc code=end

