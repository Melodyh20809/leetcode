class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)
        m=0
        for i in n:
            if i=="1":
                m=m+1
        return m