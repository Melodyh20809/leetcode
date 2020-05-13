class Solution:
    def constructRectangle(self, area):
        m=int(area**0.5)
        for i in range(m,0,-1):
            if area%i==0:
                return [int(area/i),i]
        return [area,1]
x=Solution()
result=x.constructRectangle(5)
print(result)