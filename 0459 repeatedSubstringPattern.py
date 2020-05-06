
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l=len(s)
        for i in range(1,l//2+1):
            if l%i==0:
                if s[:i]*(l//i)==s:
                    return True
        return False
x=Solution()
result=x.repeatedSubstringPattern("asdfasdfasdf")
print(result)