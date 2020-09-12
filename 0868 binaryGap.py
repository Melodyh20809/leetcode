class Solution:
    def binaryGap(self, N: int) -> int:
        N=bin(N)[2:]
        d=[0]*len(N)
        a=0
        for i,j in enumerate(N):
            if j=="1":
                d[i]=i-a
                a=i
        return max(d)