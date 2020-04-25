class Solution:
    def fizzBuzz(self, n: int) :
        L=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                L.append("FizzBuzz")
            elif i%3==0:
                L.append("Fizz")
            elif i%5==0:
                L.append("Buzz")
            else:
                L.append(str(i))
        return L
x=Solution()
result=x.fizzBuzz(18)
print(result)