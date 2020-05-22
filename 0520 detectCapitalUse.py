class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.istitle() or word.islower():
            return True
        return False

x=Solution()

result=x.detectCapitalUse()
print(result)