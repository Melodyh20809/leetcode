class Solution:
    def twoSum(self, numbers, target) :
        L=[]
        for i in range(len(numbers)):
            if target-numbers[i] not in L:
                L.append(numbers[i])
            else:
                b=i
                break
        for i in range(len(L)):
            if L[i]==target-numbers[b]:
                a=i
        return [a+1,b+1]

x=Solution()
result=x.twoSum([1,2,5,11,14],13)
print(result)
        