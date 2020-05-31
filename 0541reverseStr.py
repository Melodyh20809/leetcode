class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N=len(s)
        n=0
        ans=""
        while n<N:
            s1=s[n:n+k]
            ans=ans+s1[::-1]+s[n+k:n+2*k]
            n=n+2*k
        return ans 
x=Solution()
result=x.reverseStr()
print(result)

