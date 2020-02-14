class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root) :
        if not root:
            return True
        h1=self.maxDepth(root.left)
        h2=self.maxDepth(root.right)
        if h1-h2>1 or h1-h2<-1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    
    def maxDepth(self, root):
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))


x=Solution()
root=TreeNode(0)
root.left=TreeNode(1)
root.right=TreeNode(1)
root.left.left=TreeNode(2)
root.left.left.left=TreeNode(3)
result=x.isBalanced(root)
print(result)