class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]==target:
                return i
            if nums[i]>target:
                return -1
        return -1