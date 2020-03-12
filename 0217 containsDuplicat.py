class Solution:
    def containsDuplicate(self, nums) :
        D={}
        for i in nums:
            if i in D:
                return True
            D[i]=0
        return False

x=Solution()
result=x.containsDuplicate([1,2,3,3])
print(result)