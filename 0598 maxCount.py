class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        a=inf
        b=inf
        for i in ops:
            a=min(a,i[0])
            b=min(b,i[1])
        return a*b