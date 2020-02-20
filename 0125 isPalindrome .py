class Solution:
    def isPalindrome(self, s) :
        a=""
        for i in s :
            if i.isalnum():
                a=a+i.lower()
        print(a)
        n=0
        N=-1
        for i in range(len(a)//2):
            if a[n]==a[N]:
                n=n+1
                N=N-1
            else:
                return False
        return True
x=Solution()
result=x.isPalindrome(".,")
print(result)
