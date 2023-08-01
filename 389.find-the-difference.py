#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sDict={}
        for char in s:
            if char not in sDict:
                sDict[char] = 1
            else:
                sDict[char] += 1
        tDict={}
        for char in t:
            if sDict.get(char,0) == 0:
                return char
            else:
                sDict[char] -= 1
        
        
# @lc code=end

