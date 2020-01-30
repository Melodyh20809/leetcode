class Solution:
    def countAndSay(self, n) :
        a="1"
        A=""
        while n-1>0:
            A=""
            n=n-1
            count=0
            name=a[0]
            for i in a:
                if i==name:
                    count=count+1 
                else:
                    A=A+str(count)+name
                    count=1
                    name=i
            A=A+str(count)+name    
            a=A
        return a

x=Solution()
result=x.countAndSay(1)
print(result)