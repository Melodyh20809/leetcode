class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans=0
        n=len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(i+2,n):
                    (x1,y1),(x2,y2),(x3,y3)=points[i],points[j],points[k]
                    ans=max(ans,0.5*abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return ans