class Solution:
    def pivotIndex(self, nums):
        if not nums:
            return -1
        if len(nums)==1:
            return 0
        l=0
        r=sum(nums[1:])
        for i in range(len(nums)-1):
            if l==r:
                return i
            l=l+nums[i]
            r=r-nums[i+1]
        if l==r:
            return len(nums)-1
        return -1
x=Solution()
result=x.pivotIndex([1])
print(result)