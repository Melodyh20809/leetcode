# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:

        self.sums = 0
        self.aa(root)
        return self.sums
    
    def aa(self, root):
        if not root:
            return 0
        left=self.aa(root.left)
        right=self.aa(root.right)
        self.sums+=abs(left - right)
        return left + right + root.val
x=Solution()
root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(2)
result=x.findTilt(root)
print(result)