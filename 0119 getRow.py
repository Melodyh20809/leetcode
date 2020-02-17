class Solution:
    def getRow(self, rowIndex) :
        l1=[1]
        while rowIndex!=0:
            rowIndex=rowIndex-1
            l2=l1
            l1=[1]
            n=0
            for i in range(len(l2)-1):
                a=l2[n]+l2[n+1]
                n=n+1
                l1.append(a)
            l1.append(1)
        return l1

        
x=Solution()
result=x.getRow(0)
print(result)