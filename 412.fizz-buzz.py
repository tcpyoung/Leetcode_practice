#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strList=[]
        for i in range(1,n+1):
            if(i%3==0 and i%5==0):
                strList.append("FizzBuzz")
            elif(i%5==0):
                strList.append("Buzz")
            elif(i%3==0):
                strList.append("Fizz")
            else:
                strList.append(str(i))
        return strList
                
        
# @lc code=end

