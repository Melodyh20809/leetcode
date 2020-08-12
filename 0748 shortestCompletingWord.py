import collections
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        licensePlate=licensePlate.replace(" ","").lower()
        num="0123456789"
        for i in num:
            licensePlate=licensePlate.replace(i,"")
        ans=""
        d=collections.Counter(licensePlate)
        n=len(licensePlate)
        for j in words:
            if len(j)<n:
                 continue
            TF=True
            d1=collections.Counter(j)
            for a in d:
                if d[a]>d1[a]:
                    TF=False
                    break
            if (not ans or len(ans)>len(j))and TF==True:
                ans=j
        return ans
x=Solution()
result=x.shortestCompletingWord()
print(result)