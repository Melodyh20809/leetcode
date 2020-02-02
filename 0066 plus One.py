class Solution:
    def plusOne(self, digits):
        n=0
        for i in reversed(digits):
            n=n-1
            if i==9:
                digits[n]=0
            else:
                digits[n]=digits[n]+1
                break
        if digits[0]==0:
            digits.insert(0,1)

        return digits

x=Solution()
result=x.plusOne([])
print(result)