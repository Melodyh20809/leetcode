class Solution(object):
    def rob(self, nums):
        a=b=0
        for i in nums:
            a,b = b, max(i+a,b)
        return b
        
x=Solution()
result=x.rob([2,3,4])
print(result)