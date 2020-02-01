class Solution:
    def lengthOfLastWord(self, s) :
        s=s.split()
        if not s:
            return 0
        a=len(s[-1])
        return a

x=Solution()
result=x.lengthOfLastWord("   ")
print(result)