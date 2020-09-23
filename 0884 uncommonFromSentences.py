class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a=A.split(" ")
        b=B.split(" ")
        d={}
        ans=[]
        for i in a:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in b:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        
        for i in d:
            if d[i]==1:
                ans.append(i)
        return ans
        