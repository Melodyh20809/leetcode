class Solution:
    def imageSmoother(self, M):
        if not M or not M[0]:
            return M
        m=len(M)
        n=len(M[0])
        ans=[[0]*n for _ in range(m)]
        for m1 in range(m):
            for n1 in range(n):
                s=0
                count=0
                for i in range(-1,2):
                    if m1+i>=0 and m1+i<m:
                        for j in range(-1,2):
                            if n1+j>=0 and n1+j<n:
                                count=count+1
                                s=s+M[m1+i][n1+j]
                ans[m1][n1]=int(s/count)
        return ans

x=Solution()
result=x.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
print(result)