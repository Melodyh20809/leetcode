class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n1,n2=len(nums),len(nums[0])
        if n1*n2!=r*c:
            return nums

        ans= [[0] * c  for a in range(r)]
        rnow,cnow = 0,0
        for i in range(n1):
            for j in range(n2):
                if cnow == c:
                    rnow += 1
                    cnow = 0
                ans[rnow][cnow] = nums[i][j]
                cnow += 1
        return ans

x=Solution()
result=x.matrixReshape([[1,2,],[3,4],[5,6],[7,8]],2,4)
print(result)