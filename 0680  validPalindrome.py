class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        n=0
        while left<right:
            if s[left]!=s[right]:
                a=s[left+1:right+1]
                b=s[left:right]
                if a==a[::-1] or b==b[::-1]:
                    return True
                else:
                    return False
            left=left+1
            right=right-1
        return True
x=Solution()
result=x.validPalindrome("ebcbbececabbacecbbcbe")
print(result)