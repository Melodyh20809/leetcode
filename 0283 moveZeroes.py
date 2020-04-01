class Solution:
    def moveZeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                nums.remove(0)
                nums.append(0)
        return nums

x=Solution()
result=x.moveZeroes([0,2,4,1,0,8,0,0])
print(result)