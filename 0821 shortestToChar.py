class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n=len(S)
        a=float(-inf)
        ans=[0]*n
        for i in range(n):
            if S[i]==C:
                a=i
            ans[i]=abs(i-a)
        a=float(-inf)
        for i in range(n-1,-1,-1):
            if S[i]==C:
                a=i
            ans[i]=min(ans[i],abs(a-i))
        return ans