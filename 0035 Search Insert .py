class Solution:
    def searchInsert(self, nums, target) :
        if not nums:
            return 0
        n=0
        for i in nums:
            if i==target or i>target:
                return n
            n=n+1
        return n

x=Solution()
result=x.searchInsert([0,1,4,5,5,6],5)
print(result)