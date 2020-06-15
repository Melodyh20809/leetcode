class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        ans=[]
        if not root:
            return ans
        l=[root]
        while l:
            p=l.pop()
            l.extend(p.children)
            ans.append(p.val)
        return ans[::-1]

