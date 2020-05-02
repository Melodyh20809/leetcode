class Solution:
    def numberOfBoomerangs(self, points):
      
        ans=0
        for i in points:
            d={}
            for j in points:
                length=(i[0]-j[0])**2+(i[1]-j[1])**2
                if length in d:
                    d[length]=d[length]+1
                else:
                    d[length]=1
            for n in d.values():
                ans=ans+(n*(n-1))
        return ans

x=Solution()
result=x.numberOfBoomerangs([[0,0],[1,0],[2,0],[3,0]])
print(result)