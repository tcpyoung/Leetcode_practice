#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str in strs:
            x=''.join(sorted(str))
            if x not in result:
                result[x]=[]
            result[x].append(str)

        ans = []
        for val in result.values():
            ans.append(val)
        return ans           
# @lc code=end

