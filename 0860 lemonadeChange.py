class Solution:
    def lemonadeChange(self, bills):
        d={5:0,10:0}
        for i in bills:
            if i==5:
                d[5]=d[5]+1
            elif i==10:
                if d[5]>=1:
                    d[5]=d[5]-1
                else:
                    return False
                d[10]=d[10]+1
            else:
                if d[10]>=1 and d[5]>=1:
                    d[10]=d[10]-1
                    d[5]=d[5]-1
                elif d[5]>=3:
                    d[5]=d[5]-3
                else:
                    return False
        return True
x=Solution()
result=x.lemonadeChange([5,5,10,10,20])
print(result)