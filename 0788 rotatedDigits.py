class Solution:
    def rotatedDigits(self, N: int) -> int:
        a=[2,5,6,9]
        b=[3,4,7]
        ans=0
        for i in range(2,N+1):
            A="F"
            B="T"
            for j in b:
                if str(j) in str(i):
                    B="F"
                    break
            for j in a:
                if str(j) in str(i):
                    A="T"
                    break          
            if A=="T" and B=="T":
                ans=ans+1
        return ans
                
            