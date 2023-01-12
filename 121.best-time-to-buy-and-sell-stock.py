#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy=10001
        for price in prices:
            if(price<buy): buy=price
            if(price-buy>profit): profit=price-buy

        return profit
        """
        :type prices: List[int]
        :rtype: int
        """
        
# @lc code=end

