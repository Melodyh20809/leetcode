class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        ans=""
        if num<0:
            num+=1<<32
        while num!=0:
            a=num%16
            if a<10:
                ans=str(a)+ans
            else:
                ans=chr(a-10+ord("a"))+ans
            num=num//16
                
        return ans