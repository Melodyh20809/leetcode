class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a=1
        ans=[]
        n=len(nums)
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                a=a+1
            else:
                ans.append(a)
                a=1
        ans.append(a)
        return max(ans)
            
            
    