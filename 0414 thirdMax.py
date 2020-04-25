class Solution:
    def thirdMax(self, nums: List[int]) -> int: 
        n1=n2=n3=-inf #n1>n2>n3
        for i in nums:
            if i>n1:
                n1,n2,n3=i,n1,n2
            elif i>n2 and i<n1:
                n2,n3=i,n2
            elif i>n3 and i<n2:
                n3=i
        if n3!=-inf:
            return n3        
        else:
            return n1
x=Solution()
result=x.thirdMax([2,1])
print(result)