import collections
class Solution:
    def findPairs(self, nums, k):
        ans=0
        d=collections.Counter(nums) #把nums放進字典 並計算出現次數
        if k==0:
            for i in set(nums):
                if d[i]>1:
                    ans=ans+1
        if k>1:        
            for i in set(nums):
                if i+k in d:
                    ans=ans+1

        return ans

x=Solution()
result=x.findPairs([3, 1, 4, 1, 5], 2)
print(result)