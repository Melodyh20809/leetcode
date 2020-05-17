class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            a="-"
            num=-num
        else:
            a=""
        ans=""
        while num>=1:
            ans=str(num%7)+ans
            num=num//7
        ans=a+ans
        return ans
x=Solution()
result=x.convertToBase7()
print(result)