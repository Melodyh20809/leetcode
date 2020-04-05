
class NumArray:

    def __init__(self, nums: List[int]):
        self.L=[0]
        for i in range(len(nums)):
            a=self.L[i]+nums[i]
            self.L.append(a)

    def sumRange(self, i: int, j: int) -> int:
        return self.L[j+1]-self.L[i]
