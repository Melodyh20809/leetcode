class Solution:
    def findShortestSubArray(self, nums) :
        a={}
        b={}
        c={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in c:
                c[nums[i]]=1
                a[nums[i]]=i
            else:
                c[nums[i]]+=1
            b[nums[i]]=i
        n=max(c.values())
        ans=float("inf")
        for i in c:
            if c[i]==n:
                ans=min(ans,b[i]-a[i]+1)
        return ans
x=Solution()
result=x.findShortestSubArray([2])
print(result)