# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        small=min(p.val,q.val)
        big=max(p.val,q.val)
        
        if big>=root.val>=small:
            return root
        
        elif root.val>big:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val<small:
            return self.lowestCommonAncestor(root.right,p,q)

x=Solution()
T=TreeNode(6)
T.left=TreeNode(2)
T.right=TreeNode(8)
p=TreeNode(2)
q=TreeNode(8)
result=x.lowestCommonAncestor(T,p,q)
print(result)