# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        a=root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(a)
        return root
x=Solution()
root=TreeNode(0)
root.left=TreeNode(1)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(5)
root.right.right=TreeNode(6)
print(x.invertTree(root))