class Solution():
    def isHappy(self, n):
        l=[0]
        while True:
            a=0
            while n>0:
                a=a+(n%10)*(n%10)
                n=n//10
            if a==1:
                return True
            if a in l:
                return False
            else:
                l.append(a)
                n=a
            

x=Solution()
result=x.isHappy(19)
print(result)     
        