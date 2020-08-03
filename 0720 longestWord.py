class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        s=set([""])
        ans=""
        for i in words:
            if i[:-1] in s:
                s.add(i)
                if len(i)>len(ans):
                    ans=i
        return ans