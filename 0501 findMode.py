# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        count=collections.defaultdict(int)
        
        def add(root):
            if root:
                count[root.val]=count[root.val]+1
                add(root.left)
                add(root.right)
        
        add(root)
        m=max(count.values())
        l=[]
        for i in count :
            if count[i]==m:
                l.append(i)
        return l
x=Solution()
r=TreeNode(1)
r.left=TreeNode(1)
r.right=TreeNode(2)
r.left.left=TreeNode(2)
result=x.findMode(r)
print(result)
