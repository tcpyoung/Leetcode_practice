#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s)-1

        while left < right:
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
# @lc code=end

