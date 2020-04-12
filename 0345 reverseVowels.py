class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return ""
        L=["a","e","i","o","u","A","E","I","O","U"]
        s=list(s)
        n1=-1
        n2=len(s)
        while n2>n1:
            n1=n1+1
            n2=n2-1
            while s[n1] not in L and n2>n1:
                n1=n1+1
            while s[n2] not in L and n2>n1:
                n2=n2-1
            if n2>n1:
                s[n1],s[n2]=s[n2],s[n1]
        return "".join(s)
x=Solution()
result=x.reverseVowels("")
print(result)