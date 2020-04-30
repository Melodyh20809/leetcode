class Solution(object):
    def arrangeCoins(self, n):
        a,b=0,n+1 
        while a<b:
            mid=(a+b)// 2
            if mid * (mid + 1)/2 <=n:
                a=mid+1
            else:
                b=mid
        return a-1
x=Solution()
result=x.arrangeCoins(100)
print(result)