#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result={}
        for num in nums:
            if num not in result:
                result[num]=1
            else:
                result[num]+=1
        return sorted(result,key=result.get,reverse=True)[0:k]
# @lc code=end

