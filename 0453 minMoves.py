class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-len(nums)*min(nums)
x=Solution()
result=x.minMoves()
print(result)