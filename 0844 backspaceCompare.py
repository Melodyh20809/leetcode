class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s=""
        t=""
        for i in S:
            if i=="#":
                s=s[:-1]
            else:
                s=s+i
        for j in T:
            if j=="#":
                t=t[:-1]
            else:
                t=t+j
        if s==t:
            return True
        else:
            return False
x=Solution()
result=x.backspaceCompare("ab#c","ad#c")
print(result)