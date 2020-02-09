class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

x=Solution()
p=TreeNode(1)
p.left=TreeNode(2)
p.left.left=TreeNode(5)
p.right=TreeNode(3)

q=TreeNode(1)
q.left=TreeNode(2)
q.left.left=TreeNode(5)
q.right=TreeNode(4)


result=x.isSameTree(p,q)
print(result)
