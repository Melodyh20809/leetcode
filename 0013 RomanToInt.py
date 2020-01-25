class Solution:
    def romanToInt(self, s: str) -> int:
        n={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        A=0
        a=0
        s=s[::-1]
        for i in s:
            if n[i]>=a:
                a=n[i]
                A=A+a
            if n[i]<a:
                a=n[i]
                A=A-a
        return A

x=Solution()
result=romanToInt("MCMXCIV")
print(result)