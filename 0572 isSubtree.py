# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if self.check(s, t)==True: 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def check(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)