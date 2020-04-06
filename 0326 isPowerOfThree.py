class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1162261467 = 3的19次方 (3的20次方>2的31次方)
        
        if n>0 and 1162261467%n==0:
            return True
        else:
            return False