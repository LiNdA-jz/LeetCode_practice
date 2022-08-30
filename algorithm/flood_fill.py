class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # not work
        r, c = sr, sc

        color_list = [[sr,sc]]
        while (r>=0 and c>=0):
            if (r>0):
                if (image[r,c]==image[sr,sc]):
                    r -= 1
                    color_list.append([r, c])
            if (c>0):
                if (image[r,c]==image[sr,sc]):
                    c -= 1
                    color_list.append([r, c])

        for i in color_list:
            image[color_list[i]] = color

        
        return image


        # DFS
        # Time Complexity: O(N), where NN is the number of pixels in the image. We might process every pixel.
        # Space Complexity: O(N), the size of the implicit call stack when calling dfs.

        # There are three things that you need to consider once you have identified that a question can be sovled using DFS
        # The base case ( return condition )
        # Mark that node as visited
        # Given that I am at a particular node what operations do I need to perform
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image