class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        l=[]
        for i in s:
            l.append(i[::-1])
        ans=" ".join(l)
        return ans
        
x=Solution()
result=x.reverseWords()
print(result)