
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None




class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        L=[]
        l=[]
        a=[root]
        while a:
            l=[]
            for i in range(len(a)):
                l.append(root.val) 
                if root.left:
                    a.append(root.left.val)
                if root.right:
                    a.append(root.right.val)
                del a[0]
            L.append(l)
        return L[::-1]

x=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.right=TreeNode(5)
root.right=TreeNode(3)
root.right.left=TreeNode(6)


result=x.levelOrderBottom(root)
print(result)