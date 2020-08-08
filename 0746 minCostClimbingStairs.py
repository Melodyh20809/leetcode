class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n=len(cost)
        ans=[0]*n
        ans[0]=cost[0]
        ans[1]=cost[1]
        for i in range(2,n):
            ans[i]=min(ans[i-1],ans[i-2])+cost[i]
        return ans[-1]