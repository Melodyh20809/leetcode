# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.add(root,sum)+self.add(root.left,sum)+self.add(root.right,sum)
    
    def add(self,root,sum):
        n=0
        if not root:
            return n
        sum=sum-root.val
        if sum==0:
            n=n+1
        n=n+self.add(root.right,sum)
        n=n+self.add(root.left,sum)            
        return n
x=Solution()
root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(-3)
root.left.left=TreeNode(3)
root.left.right=TreeNode(2)
root.right.right=TreeNode(11)
root.left.left.left= TreeNode(3)
root.left.left.right=TreeNode(-2)
root.left.right.right=TreeNode(1)
result=x.pathSum(root,8)
print(result)