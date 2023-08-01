#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        dp=[0]*(n+1)
        for i in range(2,n+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        
        return dp[n]
        """
        :type cost: List[int]
        :rtype: int
        """
        
# @lc code=end

