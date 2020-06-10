class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)),len(candies)//2)

x=Solution()
result=x.distributeCandies()
print(result)