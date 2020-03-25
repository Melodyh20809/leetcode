# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
         self.right = Non
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        a=[]
        if not root:
            return a
        if not root.left and not root.right:
            a.append(str(root.val))
        for i in self.binaryTreePaths(root.left):
            a.append(str(root.val)+"->"+i)
        for i in self.binaryTreePaths(root.right):
            a.append(str(root.val)+"->"+i)
        return a