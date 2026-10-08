#m=no. of rows
#n=no. of coln
#O(m*n) time complexity
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        checkimg = [[False for inneritem in item] for item in image]  # to make sure we dont visit any pixel twice
        origcol = image[sr][sc]  # color of starting pixel
        tr = len(image)  # total row
        tc = len(image[0])  # total column

        def coloring(r, c):
            checkimg[r][c] = True
            if image[r][c] == origcol:  # check current pixel color
                image[r][c] = color
                # for neighbouring pixels
                if 0 <= r - 1 <= tr - 1 and 0 <= c <= tc - 1 and checkimg[r - 1][
                    c] == False:  # just above pixel if exists and not checked
                    coloring(r - 1, c)
                if 0 <= r + 1 <= tr - 1 and 0 <= c <= tc - 1 and checkimg[r + 1][
                    c] == False:  # just below pixel if exists and not checked
                    coloring(r + 1, c)
                if 0 <= r <= tr - 1 and 0 <= c - 1 <= tc - 1 and checkimg[r][
                    c - 1] == False:  # just left pixel if exists and not checked
                    coloring(r, c - 1)
                if 0 <= r <= tr - 1 and 0 <= c + 1 <= tc - 1 and checkimg[r][
                    c + 1] == False:  # just right pixel if exists and not checked
                    coloring(r, c + 1)

        coloring(sr, sc)
        return image