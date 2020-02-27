class Solution:
    def convertToTitle(self, n: int) -> str:
        ans=""
        while n:
            a=chr((n-1)%26+65)
            ans=a+ans
            n=(n-1)//26
        return ans

x=Solution()
result=x.convertToTitle(26)
print(result)

