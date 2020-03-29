class Solution:
    def isBadVersion(self,n):
        if n<1:
            return False
        if n>=1:
            return True
        

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1=n//2
        while self.isBadVersion(n1)!=True or self.isBadVersion(n1-1)!=False:
            if self.isBadVersion(n1)==False:
                if n-n1<=1:
                    n1=n1+1
                else:
                    n1=(n+n1)//2
            else:
                n=n1
                n1=n1//2
        return n1

x=Solution()
result=x.firstBadVersion(1000)
print(result)            
        
    
        