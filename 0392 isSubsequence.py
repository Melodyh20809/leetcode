class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        n=0
        for i in t:
            if i==s[n]:
                n=n+1
            if n==len(s):
                return True
        return False

x=Solution()
result=x.isSubsequence("ace","ahbgdc")
print(result)