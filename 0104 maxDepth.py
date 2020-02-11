class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))








x=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.left.left=TreeNode(8)
root.left.right=TreeNode(3)
root.right=TreeNode(2)
root.right.left=TreeNode(3)


result=x.maxDepth(root)
print(result)