class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d={}
        
        ans=[]
        for i in "qwertyuiopQWERTYUIOP":
            d[i]=1
        for i in "asdfghjklASDFGHJKL":
            d[i]=2
        for i in "zxcvbnmZXCVBNM":
            d[i]=3
        for i in words:
            a=""
            for j in i:
                a=a+str(d[j])
            if len(set(a))==1:
                ans.append(i)
        return ans