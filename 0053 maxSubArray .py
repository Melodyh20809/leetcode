class Solution:
    def maxSubArray(self, nums):
        s=0
        m=-2147483648
        for i in nums:
            s=s+i
            s=max(s,i)
            m=max(m,s)
        return m    

x=Solution()
result=x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)         