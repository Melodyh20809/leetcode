class Solution:
    def canPlaceFlowers(self, flowerbed, n) :
        N=0
        m=0
        flowerbed=[0]+flowerbed+[0]
        for i in flowerbed:
            if i==0:
                m=m+1
            else:
                N=N+int((m-1)/2)
                m=0
        N=N+int((m-1)/2)     
        if N>=n:
            return True
        return False
x=Solution()
result=x.canPlaceFlowers([0,0],2)
print(result)