class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num>0:
            num=bin(num)[2:]
            if num.count("1")==1 and num.count("0")%2==0:
                return True
        else:
            return False