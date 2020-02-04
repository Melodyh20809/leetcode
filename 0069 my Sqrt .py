class Solution:
    def mySqrt(self, x) :
        n=0
        while n*n<=x:
            n=n+1
        return n-1


x=Solution()
result=x.mySqrt(1)
print(result)