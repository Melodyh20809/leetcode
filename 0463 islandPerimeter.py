class Solution:
    def islandPerimeter(self, grid) :
        lenght=len(grid)
        width=len(grid[0])
        a=0
        b=0
        for i in range(lenght):
            for j in range(width):
                if grid[i][j]==1:
                    a=a+1
                    if i<lenght-1:
                        if grid[i+1][j]==1:
                            b=b+1
                    if j<width-1:
                        if grid[i][j+1]==1:
                            b=b+1
        return a*4-b*2
        
x=Solution()
result=x.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(result)