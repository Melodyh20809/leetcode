class Solution:
    def  missingNumber(self, nums: List[int]) -> int:
        a=(1+nums[-1])*(len(nums)-1)/2
        b=0
        for i in nums:
            b=b+i
        return a-b

x=Solution()
result=x.missingNumber()
print(result)