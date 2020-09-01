class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        [A, B, C, D]=rec1
        [E, F, G, H]=rec2
        x=min(C,G)-max(A,E)
        y=min(D,H)-max(B,F)
        if x>0 and y>0:
            return True
        return False
           