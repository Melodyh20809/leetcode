
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum=sum-root.val
        if sum==0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        

x=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(20)
root.left.left=TreeNode(3)
root.left.right=TreeNode(30)
root.right.left=TreeNode(30)
root.left.left.left=TreeNode(4)
sum=10
result=x.hasPathSum(root,sum)
print(result)