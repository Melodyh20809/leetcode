class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        L1=list(secret)
        L2=list(guess)
        A=0
        B=0
        i=0
        while i<len(L1):
            if L1[i]==L2[i]:
                A=A+1
                L1.remove(L1[i])
                L2.remove(L2[i])
            else:
                i=i+1
        
        for i in L2:
            if i in L1:
                B=B+1
                L1.remove(i)
        return str(A)+"A"+str(B)+"B"
x=Solution()
result=x.getHint("011","011")
print(result)
