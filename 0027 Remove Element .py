class Solution:
    def removeElement(self, nums, val):
        n=0
        while n!=len(nums):
            if nums[n]==val:
                nums.remove(nums[n])
            else:
                n=n+1
        lenght=len(nums)
        return lenght
x=Solution()
result=x.removeElement([0,1,2,2,3,4,2,1,2],)
print(result)
