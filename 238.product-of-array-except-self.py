#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        
        result = [1 for _ in range(len(nums))]
        n=len(nums)
        prefix_product=1
        #result[0]=1 prefix =1 
        #result[1]=1 prefix =2
        #result[2]=2 prefix= 6
        #result[3]=6 prefix= 24
        for i in range(n):
            result[i]*=prefix_product
            prefix_product*=nums[i]
        postfix_product=1
        for i in range(n-1,-1,-1):         
            result[i]*=postfix_product
            postfix_product*=nums[i]
            print(result[i])
            print("***"+str(postfix_product))
        print(result)
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
# @lc code=end

