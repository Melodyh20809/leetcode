#Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans=0
        def aa(root):
            if not root:
                return 0
            left=aa(root.left)
            right=aa(root.right)
            self.ans=max(self.ans,left+right)
            return max(left,right)+1
        aa(root)
        return self.ans  

x=Solution()
root=TreeNode(0)
root.left=TreeNode(1)
root.left.left=TreeNode(2)
root.right=TreeNode(3)
root.right.right=TreeNode(4)
result=x.diameterOfBinaryTree(root)
print(result)