class Solution:
    def majorityElement(self, nums):
        L=[]
        for i in nums:
            if i not in L:
                L.append(i)
                if nums.count(i)>len(nums)/2:
                    return i
x=Solution()
result=x.majorityElement([1,4,2,6,4,3,4,4,5,4,4,3,4])
print(result)