class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1

x=Solution()
result=x.firstUniqChar("loveleetcode")
print(result)