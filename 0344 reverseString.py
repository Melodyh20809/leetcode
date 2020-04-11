class Solution:
    def reverseString(self, s=List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            a=s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1]=a
            
x=Solution()
result=x.reverseString(["a","b","c"])
print(result)