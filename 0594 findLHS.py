from collections import Counter
class Solution:
    def findLHS(self, nums) :
        nums=Counter(nums)
        ans=0
        for i in nums:
            if nums[i+1]:
                ans=max(ans,nums[i]+nums[i+1])
        return ans
x=Solution()
result=x.findLHS([1,3,2,2,5,2,3,7])
print(result)