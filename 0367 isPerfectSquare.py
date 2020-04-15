class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while num>0:
            num=num-i
            i=i+2
        if num==0:
            return True
        else:
            return False
            