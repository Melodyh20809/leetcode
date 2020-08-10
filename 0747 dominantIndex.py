class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        a=max(nums)
        ans=nums.index(a)
        nums.pop(ans)
        if a>=max(nums)*2:
            return ans
        else:
            return -1