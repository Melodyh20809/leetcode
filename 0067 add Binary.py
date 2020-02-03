class Solution:
    def addBinary(self, a, b) :
        n,A,B,C=0,1,1,0
        c=""
        while -n<len(a) or-n<len(b):
            n=n-1
            if -n<=len(a):
                A=int(a[n])
            else:
                A=0
            if -n<=len(b):
                B=int(b[n])
            else:
                B=0
            if A+B+C==0:
                c=c+"0"
                C=0
                continue
            if A+B+C==1:
                c=c+"1"
                C=0
                continue
            if A+B+C==2:
                c=c+"0"
                C=1
                continue
            if A+B+C==3:
                c=c+"1"
                C=1
        if C==1:
            c=c+"1"
        return c[::-1]
x=Solution()
result=x.addBinary("11","11")
print(result)

            