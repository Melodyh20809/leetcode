class Solution:
    def maxProfit(self, prices) :
        if not prices:
            return 0
        min=prices[0]
        max=0
        for i in prices:
            if min>i:
                min=i
            if i-min>max:
                max=i-min
        return max
x=Solution()
result=x.maxProfit([7,6,4,3,1])
print(result)