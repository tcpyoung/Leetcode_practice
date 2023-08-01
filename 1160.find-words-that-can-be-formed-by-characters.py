#
# @lc app=leetcode id=1160 lang=python
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        charsDict={}
        res=0
        for char in chars:
            if char in charsDict:
                charsDict[char] += 1
            else:
                charsDict[char] = 1
        
        for word in words:
            wordCount = {}        
            for char in chars:
                wordCount[char] = 0
            flag = True
            for char in word:
                if char in wordCount:
                    wordCount[char] += 1
                else:
                    wordCount[char] = 1
            for k,v in wordCount.items():
                cnt=charsDict.get(k,0)
                if(v>cnt):
                    flag=False
                    break
            if(flag): res += len(word)
        
        return res
        

        
# @lc code=end

