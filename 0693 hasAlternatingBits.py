class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
            ^  ：當兩對應的二進位相異時，結果為1
            >>  :把二進位向右移 eg: 12=1100 , 12>>2 = 1100 向右移兩位 = 11 = 3 
            如果n是交錯二進位數，n^(n>>1)會是 11111......
            因為n=111... -> n+1= 1000...(用 & 會全部變零)
        """
        n=n^(n>>1) 
        if n & (n+1)==0:
            return True
        else:
            return False
            
x=Solution()
result=x.hasAlternatingBits(5)
print(result)