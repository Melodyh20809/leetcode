class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans=0
        for i in S:
            if i in J:
                ans=ans+1
        return ans 