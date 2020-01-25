class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':0, ')':1, '{':0, '}':1, '[':0 ,']':1}
        D={'(':1, ')':1, '{':2, '}':2, '[':3 ,']':3}
        a=0
        A=0
        b=10
        if len(s)%2==1:
            A=1
        while len(s)!=0 and A==0:
            n=0
            for i in s:
                if d[i]==a:
                    a=d[i]
                    b=D[i]
                    n=n+1
                if n==len(s):
                    A=1
                if d[i]!=a:
                    if D[i]==b:
                        s=s[:n-1]+s[n+1:]
                        break
                    else:
                        A=1
                        break
        if len(s)==0 and A==0:
            return True
        else:
            return False


x=Solution()
result=x.isValid("((")
print(result)

