class Solution:
    def findErrorNums(self, nums):
        nums.sort()
        n=len(nums)
        nums=[0]+nums+[n+1]
        ans=[]
        for i in range (n+1):
            if nums[i]==nums[i+1]:
                ans.insert(0,nums[i])
                continue
            if nums[i]+1!=nums[i+1]:
                ans.append(nums[i]+1)    
        return ans
x=Solution()
result=x.findErrorNums([1,3,4,5,5])
print(result)