class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        n=0
        ans=[]
        for i in nums2:
            d[i]=n
            n=n+1
        l=n+2
        for i in nums1:
            n=d[i]
            for j in nums2[n:l]:
                if j>i:
                    ans.append(j)
                    break
                if j==nums2[-1]:
                    ans.append(-1)
        return ans
                
                    