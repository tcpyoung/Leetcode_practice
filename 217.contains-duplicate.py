#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        record = set()
        for num in nums:
            if num in record:
                return True
            record.add(num)
        return False
           
        """
        :type nums: List[int]
        :rtype: bool
        """
        
# @lc code=end

