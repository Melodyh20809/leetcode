class Solution(object):
    def trailingZeroes(self, n):
        N=0
        m=5
        while n>=m:
            N=N+n//m
            m=m*5
        return N 
x=Solution()
result=x.trailingZeroes(1000)
print(result)