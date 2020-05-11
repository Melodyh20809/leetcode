class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S="".join(S.split("-")).upper()
        l=len(S)
        ans=[]
        if l%K>0:
            ans.append(S[:l%K])
        for i in range(l%K,l,K):
            ans.append(S[i:i+K])
        return "-".join(ans)

x=Solution()
result=x.licenseKeyFormatting("kh-hl24-2cjS-fs",3)
print(result)