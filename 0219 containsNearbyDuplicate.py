class Solution:
    def containsNearbyDuplicate(self, nums, k) :
        D={}
        for i in range(len(nums)):
            if nums[i] in D and i-D[nums[i]]<=k:
                return True
            else:
                D[nums[i]]=i
        return False


            

x=Solution()
result=x.containsNearbyDuplicate([1,0,1,1], 1)
print(result)
        