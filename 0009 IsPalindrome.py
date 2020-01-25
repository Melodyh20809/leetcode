class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            a=int(str(x)[::-1])
        else:
            x=-x
            a=int(str(x)[::-1])
            a=-a
        if a==x and a>=0:
            return True
        if a<0 or a!=x:
            return False
        