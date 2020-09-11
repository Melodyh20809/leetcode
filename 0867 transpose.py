class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n1=len(A)
        n2=len(A[0])
        ans=[[0]*n1 for i in range(n2)]
        for i in range(n1):
            for j in range(n2):
                ans[j][i]=A[i][j]
        return ans
            