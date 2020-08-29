class Solution:
    def toGoatLatin(self, S: str) -> str:
        l=["a","e","i","o","u","A","E","I","O","U"]
        ans=[]
        S=S.split(" ")
        for i in range(len(S)):
            if S[i][0] in l:
                a=S[i]+"ma"+"a"*(i+1)
            else:
                a=S[i][1:]+S[i][0]+"ma"+"a"*(i+1)
            ans.append(a)
        return " ".join(ans)
             
                