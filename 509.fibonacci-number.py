#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start


class Solution(object):
    def fib(self, n):
        if (n==0):
            return 0

        dp = [0] * (n+1)

        dp[0]=0
        dp[1]=1
        
        for i in range (2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        

        return dp[n]


        """
        :type n: int
        :rtype: int
        """
        
# @lc code=end

