class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        a=len(A)
        b=len(B)
        n=b//a+2
        for i in range(1,n+1):
            if B in A*i:
                return i
        return -1