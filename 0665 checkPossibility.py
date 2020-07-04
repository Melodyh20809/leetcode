class Solution:
    def checkPossibility(self, nums):
        n=0
        nums=[-10000]+nums+[10000,10000]
        for i in range(1,len(nums)-2):
            if nums[i]>nums[i+1]:
                n=n+1
                if n>1:
                    return False
                if nums[i]<=nums[i+2]:
                    nums[i+1]=nums[i]
                    continue
                if nums[i+1]>=nums[i-1]:
                    nums[i]=nums[i+1]
                    continue
                return False
        return True
        
x=Solution()
result=x.checkPossibility([4,2,3])
print(result)
