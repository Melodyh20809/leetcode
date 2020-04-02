class Solution:
    def wordPattern(self, pattern, str):
        d1={} #pattern:str
        d2={} #str:pattern
        L=str.split()
        if len(pattern)!=len(L):
            return False
        
        for n in range(len(L)):
            if pattern[n] in d1:
                if d1[pattern[n]]!=L[n]:
                    return False
            else:
                if L[n] in d2:
                    return False
                d1[pattern[n]]=L[n]
                d2[L[n]]=pattern[n]

        return True
x=Solution()
result=x.wordPattern("abba","cat cat cat cat")
print(result)