class Solution:
    def removeDuplicates(self, nums) :
        a=int
        n=0
        while n!=len(nums) :
            if nums[n]==a:
                a=nums[n]
                nums.remove(nums[n])
            else:
                a=nums[n]
                n=n+1
        lenght=len(nums)
        return lenght
x=Solution()
result=x.removeDuplicates([1,1])
print(result)