#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxResult =0
        for customer in accounts:
            result=0
            for bank in customer:
                result += bank
            if result > maxResult:
                maxResult = result

        return maxResult   
        
# @lc code=end

