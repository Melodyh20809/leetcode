class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:
            return -1
        else:
            return max(len(a),len(b))
    
x=Solution()
result=x.findLUSlength()
print(result)
