class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}   #s:t
        dict2={}   #t:s
        for a1,a2 in zip(s,t):
            if a1 in dict1 and dict1[a1]!=a2:
                return False
            if a2 in dict2 and dict2[a2]!=a1:
                return False
            dict1[a1]=a2
            dict2[a2]=a1
        return True

x=Solution()
result=x.isIsomorphic("abb","def")
print(result)