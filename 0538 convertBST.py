class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum=0
        
        def change(r):
            if not r: 
                return
            change(r.right)
            self.sum + =r.val
            r.val = self.sum
            change(r.left)
            
        change(root)
        return root

x=Solution()
root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(12)
root.right.left=TreeNode(8)
result=x.convertBST(root)
print(result)