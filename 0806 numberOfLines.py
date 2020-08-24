class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        a=0
        ans=0
        for i in S:
            s=widths[ord(i)-97]
            if a+s<=100:
                a=a+s
            else:
                a=s
                ans=ans+1
        ans=ans+1
        return [ans,a]