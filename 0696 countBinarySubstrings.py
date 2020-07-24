class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n=len(s)
        m=1
        l=[]
        for i in range(1,n):
            if s[i]==s[i-1]:
                m=m+1
            else:
                l.append(m)
                m=1
        l.append(m)
        N=len(l)
        ans=0
        for j in range(1,N):
            ans=ans+min(l[j],l[j-1])
        return ans

x=Solution()
result=x.countBinarySubstrings("00110")
print(result)