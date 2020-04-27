class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans=""
        n=0
        A=len(num1)
        B=len(num2)
        if A>=B:
            num2="0"*(A-B)+num2
            m=A 
        if A<B:
            num1="0"*(B-A)+num1
            m=B

        for i in range(-1,-m-1,-1):
            a=(int(num1[i])+int(num2[i]))+n
            if a>=10:
                a=a-10
                n=1
            else:
                n=0
            ans=str(a)+ans
        if n==1:
            ans="1"+ans
        return ans

x=Solution()
result=x.addStrings("92","23")
print(result)