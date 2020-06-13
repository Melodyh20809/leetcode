class Solution:
    def findUnsortedSubarray(self, nums):
        l=len(nums)
        n=sorted(nums)
        if nums==n:
            return 0
        for i in range(l):
            if nums[i]!=n[i]:
                a=i
                break
        for i in range(l-1,-1,-1):
            if nums[i]!=n[i]:
                b=i
                break
        return b-a+1

x=Solution()
result=x.findUnsortedSubarray([2,6,4,8,10,9,15])
print(result)
                
            