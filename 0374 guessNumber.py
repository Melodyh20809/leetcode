# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution(object):
    def guessNumber(self, n:int)->int:
        
        small=1
        big=n
        while True:
            mid=(small+big)/2
            if self.guess(mid) == 1:
                small=mid+1
            if self.guess(mid)==-1:
                big=mid-1
            if self.guess(mid)==0:
                return int(mid)
    def guess(self,m):
        ans=10
        if m>ans:
            return -1
        if m<ans:
            return 1
        if m==ans:
            return 0

x=Solution()
result=x.guessNumber(21)
print(result)