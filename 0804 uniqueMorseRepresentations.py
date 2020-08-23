class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]  
        ans=[]
        for i in words:
            a=""
            for j in i:
                a=a+l[ord(j)-97]
            if a not in ans:
                ans.append(a)
        return len(ans)