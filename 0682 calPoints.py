class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l=[]
        for i in ops:
            if i=="C":
                l.pop()
            elif i=="D":
                a=(l[-1])*2
                l.append(a)
            elif i=="+":
                l.append(l[-1]+l[-2])
            else:
                l.append(int(i))
        return sum(l)