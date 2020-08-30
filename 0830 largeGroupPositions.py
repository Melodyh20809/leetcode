class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S)<=1:
            return []
        ans=[]
        a=0
        for i in range(1,len(S)):
            if S[i]!=S[i-1]:
                if i-a>=3:
                    ans.append([a,i-1])
                a=i
        if i-a>=2:
            ans.append([a,i])
        return ans