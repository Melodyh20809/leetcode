class Solution:
    def fib(self, N: int) -> int:
        if N==0 or N==1:
            return N
        a=0
        b=1
        for i in range(1,N):
            a,b=b,a+b
        
        return b 