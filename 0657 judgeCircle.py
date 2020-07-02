import collections
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=collections.Counter(moves)
        if a["U"]==a["D"] and a["L"]==a["R"]:
            return True
        return False