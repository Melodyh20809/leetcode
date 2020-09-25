class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a=sum(A)
        b=sum(B)
        ave=(a+b)/2
        B=set(B)
        for i in A:
            c=ave-(a-i)  #所求的和-(目前除去i後的總和)
            if c in B:
                return [i,c]