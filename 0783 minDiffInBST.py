class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def aa(root1):
            if not root1:
                return []
            return aa(root1.left)+[root1.val]+aa(root1.right)
        ans=float("inf")
        l=aa(root)
        for i in range(1,len(l)):
            ans=min(ans,l[i]-l[i-1])
        return ans