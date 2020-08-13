class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        l=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        ans=0
        for i in range(L,R+1):
            a=bin(i)
            if a.count("1") in l:
                ans=ans+1
        return ans