#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sDict={}
        for char in s:
            sDict[char]= sDict.get(char,0)+1
        for char in t:
            if char not in sDict or sDict[char]==0:
                return False
            sDict[char] -= 1
        return True
# @lc code=end

