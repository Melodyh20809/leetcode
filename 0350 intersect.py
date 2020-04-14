class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        nums1.sort()
        nums2.sort()
        n1=0
        n2=0
        while n1<len(nums1) and n2<len(nums2):
            if nums1[n1]<nums2[n2]:
                n1=n1+1
                continue
            if nums1[n1]>nums2[n2]:
                n2=n2+1
                continue
            if nums1[n1]==nums2[n2]:
                l.append(nums1[n1])
                n1=n1+1
                n2=n2+1
        return l       
