class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        m=nums[len(nums)//2]
        root=TreeNode(m)
        root.left = self.sortedArrayToBST(nums[:nums[len(nums)//2]])
        root.right = self.sortedArrayToBST(nums[nums[len(nums)//2]+1:])
        return root
        
        
    

x=Solution()
#result=x.sortedArrayToBST([])
result=x.sortedArrayToBST([-10,-5,-3,0,5,9])
print(result)