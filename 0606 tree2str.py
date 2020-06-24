# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        ans=str(t.val)
        if t.left or t.right:
            ans=ans+"("+self.tree2str(t.left)+")"
        if t.right:
            ans=ans+"("+self.tree2str(t.right)+")"
        return ans 