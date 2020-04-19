class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        d={}
        for i in magazine:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in ransomNote:
            if i not in d:
                return False
            d[i]=d[i]-1
            if d[i]<0:
                return False
        return True

x=Solution()
result=x.canConstruct("aa","aab")
print(result)