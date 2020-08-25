class Solution:
    def subdomainVisits(self, cpdomains) :
        d={}
        for i in cpdomains:
            t=i.split(" ")
            time=int(t[0])
            l=t[1].split(".")
            for j in range(len(l)):
                a=".".join(l[j:])
                if a in d:
                    d[a]=d[a]+time
                else:
                    d[a]=time
        l1=list(d.keys())
        l2=list(d.values())
        ans=[]
        for i in range(len(l1)):
            b=str(l2[i])+" "+l1[i]
            ans.append(b)
        return ans
x=Solution()
result=x.subdomainVisits(["9001 discuss.leetcode.com"])
print(result)