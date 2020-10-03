class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        a=set()
        for i in A:
            a.add("".join(sorted(i[0::2]))+"".join(sorted(i[1::2])))
        return len(a)