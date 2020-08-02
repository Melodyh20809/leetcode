class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n=0
        while n<len(bits)-1:
            if bits[n]==0:
                n=n+1
            else:
                n=n+2
        if n==len(bits)-1:
            return True
        else:
            return False
        