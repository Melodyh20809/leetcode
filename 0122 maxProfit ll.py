class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        a=prices[0]
        A=0
        for i in prices[1:]:
            if i>a:
                A=A+i-a
            a=i
        return A


