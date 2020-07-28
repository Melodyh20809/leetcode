class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.n=len(self.nums)
        self.k=k
        heapq.heapify(self.nums)
        while self.n>k:
            self.n-=1
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if self.n<self.k:
            self.n+=1
            heapq.heappush(self.nums,val)
        elif val>self.nums[0]:
            heapq.heapreplace(self.nums,val)
        return self.nums[0]