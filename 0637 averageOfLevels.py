class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution:
    def averageOfLevels(self, root: TreeNode) :
        ans=[]
        r = collections.deque()
        r.append(root)
        while r:
            n=len(r)
            m=[]
            for i in range(n):
                a=r.popleft()
                if not a:
                    continue
                m.append(a.val)
                r.append(a.left)
                r.append(a.right)
            if m:
                ans.append(sum(m)/float(len(m)))
        return ans
x=Solution()
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
result=x.averageOfLevels(root)
print(result)
