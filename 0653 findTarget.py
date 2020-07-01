class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        l=[root]
        s=set()
        for i in l:
            if k-i.val in s:
                return True
            s.add(i.val)
            if i.left:
                l.append(i.left)
            if i.right:
                l.append(i.right)
        return False