class Solution:
    def getMinimumDifference(self, root):
        if not root:
            return 0
        l=[]
        ans=inf
        
        def aa(root):
            if root: #由小排到大
                aa(root.left)
                l.append(root.val)
                aa(root.right)
        aa(root)
        
        for i in range(1,len(l)):
            ans=min(ans,l[i]-l[i-1])
        return ans



x=Solution()

result=x.getMinimumDifference(root)
print(result)

     10
  8      11
7   9      12