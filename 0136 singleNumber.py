"""class Solution:
    def singleNumber(self, nums) :
        L=[]
        for i in nums:
            if i in L:
                L.remove(i)
            else:
                L.append(i)
        return L[0]
"""
class Solution:
    def singleNumber(self, nums) :
        res = 0
        for i in nums:
            res ^= i
        return res
x=Solution()
result=x.singleNumber([3,2,1,3,1])
print(result)
