#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans=0
        self.aa(root)
        return self.ans
   
    def aa(self,root):
        if not root:
            return 0
        left=self.aa(root.left)
        right=self.aa(root.right)
        l=0
        r=0
        if root.left and root.left.val==root.val:
            l=1+left
        if root.right and root.right.val==root.val:
            r=1+right
        self.ans=max(self.ans,l+r)
        return max(l,r)
x=Solution()
root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(5)