class Solution:
    def floodFill(self, image, sr, sc, newColor):
        n=len(image)
        m=len(image[0])
        color=image[sr][sc]
        if color==newColor:
            return image
        def aa(sr,sc):
            if image[sr][sc]==color:
                image[sr][sc]=newColor
                if sr>=1:
                    aa(sr-1,sc)
                if sr<n-1:
                    aa(sr+1,sc)
                if sc>=1:
                    aa(sr,sc-1)
                if sc<m-1:
                    aa(sr,sc+1)  
        aa(sr,sc)
        return image
x=Solution()
result=x.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
print(result)