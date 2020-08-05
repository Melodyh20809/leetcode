class Solution:
    def selfDividingNumbers(self, left: int, right: int) :
        ans=[]
        b="T"
        for i in range(left,right+1):
            for j in str(i):
                if j=="0" or i%int(j)!=0:
                    b="F"
                    break
            if b=="T":
                ans.append(i)
            else:
                b="T"
        return ans

x=Solution()
result=x.selfDividingNumbers(1,22)
print(result)