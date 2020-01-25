class Solution:
    def twoSum(self, nums, target) :
        h={}
        h1={}
        n1=0
        for i in nums:
            h1={i:n1}      
            n=target-i
            if n in h:
                return[h[n],n1]
            else :
                h.update(h1)
            n1=n1+1

x = Solution()
result = x.twoSum([2,7,11,18],29) 
print(result)
