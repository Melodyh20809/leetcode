class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:
            return True
        for i in range(1,int(c**0.5)+1):
            a=c-i*i
            if int(a**0.5)**2==a:
                return True
        return False