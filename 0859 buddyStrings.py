class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        l=[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                l.append(i)
        if len(l)==2:
            if A[l[0]]==B[l[1]] and  A[l[1]]==B[l[0]]:
                return True
        elif not l:
            l1=[]
            if len(A)>=2:
                for j in A:
                    if j in l1:
                        return True
                    l1.append(j)
        return False