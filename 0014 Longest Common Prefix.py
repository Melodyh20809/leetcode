class Solution:
    def longestCommonPrefix(self, strs) :
        n=0
        B=0
        A=""
        if strs!=[]:
            for i in strs:
                if len(i)==0:
                    B=1
            while B==0 and n!=len(strs[0]):    
                a=strs[0][n]
                N=0
                for i in strs:
                    if n!=len(strs[N]):
                        if i[n]==a:
                            a=i[n]
                        else:
                            B=1
                            a=""
                    else:
                        B=1
                        a=""
                    N=N+1
                A=A+a
                n=n+1   
        return A                
x=Solution()
#result=x.longestCommonPrefix(["",""])
#print(result)