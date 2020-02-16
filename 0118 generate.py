class Solution:
    def generate(self, numRows):
        if numRows==0:
            return []
        L=[[1]]
        l1=[1]
        while numRows!=1:
            numRows=numRows-1
            l2=l1
            l1=[1]
            n=0
            for i in range(len(l2)-1):
                a=l2[n]+l2[n+1]
                n=n+1
                l1.append(a)
            l1.append(1)
            L.append(l1)
        return L




x=Solution()
result=x.generate(0)
print(result)