class Solution:
    def findDisappearedNumbers(self, nums):
        L=[]
        n=len(nums)
        nums=set(nums)
        for i in range(1,n+1):
            if i not in nums:
                L.append(i)
        return L

x=Solution()
result=x.findDisappearedNumbers([2,2,3,3,4,4])
print(result)