class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        d1={}
        ans=[]
        a=inf
        for i,j in enumerate(list1):
            d[j]=i
        for i,j in enumerate(list2):
            if j in d:
                d1[j]=i+d[j]
        for i in d1:
            if d1[i]<a:
                ans=[i]
                a=d1[i]
            elif d1[i]==a:
                ans.append(i)
        return ans
                
x=Solution()
result=x.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
print(result)
    