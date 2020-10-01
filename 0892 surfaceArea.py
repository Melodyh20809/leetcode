class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans=0
        n=len(grid)
        for i in range(n):
            for j in range(n):
                ans=ans+grid[i][j]*6
                if grid[i][j]>1:
                    ans=ans-(grid[i][j]-1)*2
                if i>0:
                    ans=ans-min(grid[i][j],grid[i-1][j])*2
                if j>0:
                    ans=ans-min(grid[i][j],grid[i][j-1])*2
        return ans