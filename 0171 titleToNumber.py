class Solution:
    def titleToNumber(self, s) :
        x=0
        n=0
        for i in s[::-1]:
            x=x+(ord(i)-64)*(26**n)
            n=n+1
        return x
        

x=Solution()
result=x.titleToNumber("ALL")
print(result)

