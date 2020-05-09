class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')]+heaters+[float('inf')]
        ans=a=0
        for i in houses:
            while i>heaters[a+1]:
                a=a+1
            dis=min(heaters[a+1]-i,i-heaters[a])
            ans=max(ans,dis)
        return ans
x=Solution()
result=x.findRadius([2,1,3,4],[4,1])
print(result)