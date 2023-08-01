#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict={"}":"{",")":"(","]":"["}
        stack=[]
        for char in s:
            if char in dict.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != dict[char]:
                    return False
        return not stack
# @lc code=end

