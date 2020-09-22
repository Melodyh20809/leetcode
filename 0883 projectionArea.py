class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        a,b,c=0,0,0
        for i in grid:
            a=a+(len(i)-i.count(0))
            b=b+max(i)
        for i in zip(*grid):
            c=c+max(i)
        return a+b+c
    """
    zip(*grid): eg.[[1,2][3,4]](從y軸看過去的高度) -> [[1,3],[2,4]](從x軸看過去的高度)
    """