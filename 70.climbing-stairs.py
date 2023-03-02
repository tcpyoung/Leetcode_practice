#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        if(n<=2):
            return n
        w=[0]*(n+1)
        w[1]=1
        w[2]=2
        for i in range(3,n+1):
            w[i]=w[i-1]+w[i-2]

        return w[n]
        """
        :type n: int
        :rtype: int
        """
        
# @lc code=end

