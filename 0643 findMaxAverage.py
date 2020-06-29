class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=sum(nums[:k])
        a=ans
        n=len(nums)
        for i in range(0,n-k):
            a=a-nums[i]+nums[i+k]
            ans=max(ans,a)
        return ans/k