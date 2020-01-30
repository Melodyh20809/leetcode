"""
class Solution:
    def strStr(self, haystack, needle):
        a=""
        n=0
        N=0
        for i in haystack:
            if i==needle[n]:
                n=n+1
                a=a+i
            else:
                n=0
                a=""
            if a==needle:
                A=N-len(needle)+1
                return A
            N=N+1
        return -1 """

class Solution:
    def strStr(self, haystack, needle):
        a=""
        A=""
        n=0
        b=-1
        if not needle:
            return 0
        if len(needle)>len(haystack):
            return -1
        for i in haystack:
            b=b+1
            d=0
            if i==needle[n]:
                n=n+1
                a=a+i
                A=a
                N=n
                B=b
                while d==0 and A!=needle and B!=len(haystack)-1 :
                    B=B+1
                    if haystack[B] ==needle[N]:
                        A=A+haystack[B]
                        N=N+1
                    else:
                        d=1
                        a=""
                        n=0
            if A==needle:
                D=B-len(needle)+1
                return D
        return -1

x=Solution()
result=x.strStr("mississippi","issipi")
print(result)

            