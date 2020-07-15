# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans=set()
        self.aa(root)
        if len(self.ans)<=1:
            return -1
        m=min(self.ans)
        self.ans.remove(m)
        return min(self.ans)

    def aa(self, root):
        if not root:
            return
        self.aa(root.left)
        self.ans.add(root.val)
        self.aa(root.right)

x=Solution()
root=TreeNode(2)
root.left=TreeNode(2)
root.right=TreeNode(3)
"""root.left.left=TreeNode(2)
root.right.right=TreeNode(2)
root.left.right=TreeNode(3)
root.right.left=TreeNode(5)
"""
result=x.findSecondMinimumValue(root)
print(result)