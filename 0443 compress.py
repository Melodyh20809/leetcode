class Solution:
    def compress(self, chars) -> int:

        t=0 #放第幾個
        count=0
        s=chars[0] #存檔點
        for i in chars:
            if i==s:
                count=count+1
            else:
                chars[t]=s
                t=t+1
                if count>1:
                    for j in str(count):
                        chars[t]=j
                        t=t+1
                count=1 
                s=i
        chars[t]=s
        t=t+1
        if count>1:
            for j in str(count):
                chars[t]=j
                t=t+1
        return t
x=Solution()
result=x.compress(["a","a","a","b","b"])
print(result)