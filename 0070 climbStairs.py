"""class Solution:
    def climbStairs(self, n) :
        N,a,b,c=0,0,1,0
        while n!=N:
            c=a+b
            a=b
            b=c
            N=N+1
        return c"""

class Solution:
    def climbStairs(self, n) :


x=Solution()
result=x.climbStairs(0)
print(result)
#1,2,3,5,8,13
#1,2,3,4,5,6