class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            a=0
            while num>=1:
                a=a+num%10
                num=num//10
            num=a
        return a
x=Solution()
result=x.addDigits(38)
print(result)

        