class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m=m-1
        n=n-1
        while m+1>0 and n+1>0:
            if nums1[m]>nums2[n]:
                nums1[m+n+1]=nums1[m]
                m=m-1
            else:
                nums1[m+n+1]=nums2[n]
                n=n-1
        nums1[:n+1]=nums2[:n+1]

        return nums1
        


x=Solution()
result=x.merge([1,2,3,0,0,0],3,[2,3,5],3)
print(result)