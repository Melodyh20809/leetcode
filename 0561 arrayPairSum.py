class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=sum(nums[::2])
        return ans
