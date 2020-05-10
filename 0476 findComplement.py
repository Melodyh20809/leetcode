class Solution:
    def findComplement(self, num: int) -> int:
        num=bin(num)[2:]
        ans=""
        for i in num:
            if i=="1":
                ans=ans+"0"
            else:
                ans=ans+"1"
        return int(ans,2)

x=Solution()
result=x.findComplement(5)
print(result)
