class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=0
        ans=0
        for i in nums:
            if i==1:
                n=n+1
            else:
                n=0
            ans=max(ans,n)
        return ans
x=Solution()
result=x.findMaxConsecutiveOnes()
print(result)