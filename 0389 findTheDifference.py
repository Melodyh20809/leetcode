class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in t:
            if i not in s:
                return i
            elif d[i]==0:
                return i
            else:
                d[i]=d[i]-1
x=Solution()
result=x.findTheDifference()
print(result)        
