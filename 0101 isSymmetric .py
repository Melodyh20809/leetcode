class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.mirror(root.left,root.right)
    
    def mirror(self,left,right):
        a=left
        b=right
        if not left and not right:
            return True
        if left.val==right.val:
            return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)
        else:
            return False
        


x=Solution()

root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.left.left=TreeNode(8)
root.left.left.right=TreeNode(7)
root.left.right=TreeNode(3)
root.left.right.left=TreeNode(6)
root.left.right.right=TreeNode(5)

root.right=TreeNode(2)
root.right.left=TreeNode(3)
root.right.left.left=TreeNode(5)
root.right.left.right=TreeNode(5)
root.right.right=TreeNode(4)
root.right.right.left=TreeNode(7)
root.right.right.right=TreeNode(8)

result=x.isSymmetric(root)
print(result)