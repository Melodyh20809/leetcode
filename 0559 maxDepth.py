class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        ans=1
        for i in root.children:
            ans=max(ans,self.maxDepth(i)+1)
        return ans
        
