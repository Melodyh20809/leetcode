"""class Solution:
    def rotate(self, nums, k) :
        while k!=0:
            k=k-1
            a=nums.pop(-1)
            nums.insert(0,a)
        return nums"""
class Solution:
    def rotate1(self, nums, k) :
        a=nums[-k:]
        nums=nums[:-k]
        nums=a+nums
        return nums
x=Solution()
result=x.rotate1([1,2,3,4,5,6,7],3)
print(result)