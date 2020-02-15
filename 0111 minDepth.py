class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root) :
        if not root:
            return 0
        a=[root]
        D=0
        while a:
            D=D+1
            for i in range(len(a)):
                A=a.pop(0)
                if A.left:
                    a.append(A.left)
                if A.right:
                    a.append(A.right)
                if not A.left and not A.right:
                    return D

x=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(3)
root.right.left=TreeNode(3)
root.left.left.left=TreeNode(4)




result=x.minDepth(root)
print(result)