class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n=bin(x^y)
        return n.count("1")
x=Solution()
result=x.hammingDistance(1,4)
print(result) 
