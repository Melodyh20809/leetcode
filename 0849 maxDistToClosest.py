class Solution:
    def maxDistToClosest(self, seats) -> int:
        a=float("inf")
        ans=[0]*len(seats)
        for i in range(len(seats)):
            if seats[i]==1:
                a=i
            else:
                ans[i]=abs(i-a)
        a=float("-inf")
        for i in range(len(seats)-1,-1,-1):
            if seats[i]==1:
                a=i
            else:
                ans[i]=min(ans[i],abs(i-a))
        return max(ans)

x=Solution()
result=x.maxDistToClosest([0,0,0,1])
print(result)