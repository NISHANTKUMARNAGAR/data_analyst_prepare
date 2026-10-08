#using 2d list visited like floodfill------------------------------------------------
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        visited=[[False for inneritem in item] for item in grid]
        tr=len(grid)    #total row
        tc=len(grid[0]) #total column

        #dfs recursive method to count islands
        def countislands(i,j):
            visited[i][j]=True
            if grid[i][j]=='0': #water pixel
                return
            else:               #land pixel
                #check for its left,right,up,down pixels if they exist
                if 0<= i-1 <=tr-1 and 0<= j <=tc-1 and visited[i-1][j]==False:
                #just above pixel if exists and not checked
                    countislands(i-1,j)
                if 0<= i+1 <=tr-1 and 0<= j <=tc-1 and visited[i+1][j]==False:
                #just below pixel if exists and not checked
                    countislands(i+1,j)
                if 0<= i <=tr-1 and 0<= j-1 <=tc-1 and visited[i][j-1]==False:
                #just left pixel if exists and not checked
                    countislands(i,j-1)
                if 0<= i <=tr-1 and 0<= j+1 <=tc-1 and visited[i][j+1]==False:
                    #just right pixel if exists and not checked
                    countislands(i,j+1)


        #to go over every pixel in grid
        for i in range(tr):
            for j in range(tc):
                if visited[i][j]==False:
                    if grid[i][j]=='1': #its new land pixel
                        islands=islands+1
                    countislands(i,j)

        return islands


#using set for membership(i.e. visited or not)-----------------------------------
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        visited=set()
        tr=len(grid)    #total row
        tc=len(grid[0]) #total column

        #dfs recursive method to count islands
        def countislands(i,j,name):
            visited.add(name)
            if grid[i][j]=='0': #water pixel
                return
            else:             #land pixel
                #check for its left,right,up,down pixels if they exist
                if 0<= i-1 <=tr-1 and 0<= j <=tc-1 and (i-1,j) not in visited: #just above pixel if exists and not checked
                    countislands(i-1,j,(i-1,j))
                if 0<= i+1 <=tr-1 and 0<= j <=tc-1 and (i+1,j) not in visited: #just below pixel if exists and not checked
                    countislands(i+1,j,(i+1,j))
                if 0<= i <=tr-1 and 0<= j-1 <=tc-1 and (i,j-1) not in visited: #just left pixel if exists and not checked
                    countislands(i,j-1,(i,j-1))
                if 0<= i <=tr-1 and 0<= j+1 <=tc-1 and (i,j+1) not in visited: #just right pixel if exists and not checked
                    countislands(i,j+1,(i,j+1))


        #to go over every pixel in grid
        for i in range(tr):
            for j in range(tc):
                #dont do name=str(i)+str(j) as then
                #i=1,j=11 becomes '111' and i=11,j=1 becomes same '111' which makes confustion in visited set so use tuple(i,j)
                if (i,j) not in visited:
                    if grid[i][j]=='1': #its new land pixel
                        islands=islands+1
                    countislands(i,j,(i,j))

        return islands


#used no set or 2d list but put encountered land as water to avoid recheck
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        tr=len(grid)    #total row
        tc=len(grid[0]) #total column

        #dfs recursive method to count islands
        def countislands(i,j):
            grid[i][j]='0'
            #check for its left,right,up,down pixels if they exist
            if 0<= i-1 <=tr-1 and 0<= j <=tc-1 and grid[i-1][j]=='1': #just above pixel if exists and not checked
                countislands(i-1,j)
            if 0<= i+1 <=tr-1 and 0<= j <=tc-1 and grid[i+1][j]=='1': #just below pixel if exists and not checked
                countislands(i+1,j)
            if 0<= i <=tr-1 and 0<= j-1 <=tc-1 and grid[i][j-1]=='1': #just left pixel if exists and not checked
                countislands(i,j-1)
            if 0<= i <=tr-1 and 0<= j+1 <=tc-1 and grid[i][j+1]=='1': #just right pixel if exists and not checked
                countislands(i,j+1)


        #to go over every pixel in grid
        for i in range(tr):
            for j in range(tc):
                if grid[i][j]=='1': #its new land pixel
                    islands=islands+1
                    countislands(i,j)

        return islands