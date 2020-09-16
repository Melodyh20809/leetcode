# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1=[]
        l2=[]
        self.aa(root1,l1)
        self.aa(root2,l2)
        if l1==l2:
            return True
        return False
        
    def aa(self,root,l):
        if not root:
            return
        self.aa(root.left,l)
        if not root.left and not root.right:
            l.append(root.val)
        self.aa(root.right,l)        