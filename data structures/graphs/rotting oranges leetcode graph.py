#best one practically O(m*n) processing each orange once using list rotten-----------------------------------------
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        tr = len(grid)
        tc = len(grid[0])
        rotten = []

        # take all rotten oranges in list 'rotten'
        for i in range(tr):
            for j in range(tc):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        # make all unrotten ones adjacent to rotten rotten and increase minutes by 1
        newrotten = []
        while len(rotten) != 0:
            f = 0
            for orange in rotten:
                rr, rc = orange[0], orange[1]
                # check all neighbouring good oranges and make them rotten
                if 0 <= rr - 1 <= tr - 1 and 0 <= rc <= tc - 1 and grid[rr - 1][rc] == 1:
                    grid[rr - 1][rc] = 2
                    newrotten.append((rr - 1, rc))
                    f = 1
                if 0 <= rr + 1 <= tr - 1 and 0 <= rc <= tc - 1 and grid[rr + 1][rc] == 1:
                    grid[rr + 1][rc] = 2
                    newrotten.append((rr + 1, rc))
                    f = 1
                if 0 <= rr <= tr - 1 and 0 <= rc - 1 <= tc - 1 and grid[rr][rc - 1] == 1:
                    grid[rr][rc - 1] = 2
                    newrotten.append((rr, rc - 1))
                    f = 1
                if 0 <= rr <= tr - 1 and 0 <= rc + 1 <= tc - 1 and grid[rr][rc + 1] == 1:
                    grid[rr][rc + 1] = 2
                    newrotten.append((rr, rc + 1))
                    f = 1

            if f == 1:  # any one good orange became rotten
                minutes = minutes + 1
            rotten = newrotten.copy()
            newrotten.clear()

        # if any unrotten even after while loop return -1
        for i in range(tr):
            for j in range(tc):
                if grid[i][j] == 1:
                    return -1

        # if all unrotten became rotten and did not return -1 then return minutes took to make them rotten
        return minutes

#proper bfs using deque but still O(m*n)----------------------------------------------------------------------
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # proper bfs queue approach
        from collections import deque
        rotten = deque()
        minutes = 0
        tr = len(grid)
        tc = len(grid[0])

        # take all rotten oranges in list 'rotten'
        for i in range(tr):
            for j in range(tc):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        # make all unrotten ones adjacent to rotten rotten and increase minutes by 1
        while len(rotten) != 0:
            f = 0
            for _ in range(len(rotten)):  # while one layer lasts
                orange = rotten.popleft()
                rr, rc = orange[0], orange[1]
                # check all neighbouring good oranges and make them rotten
                if 0 <= rr - 1 <= tr - 1 and 0 <= rc <= tc - 1 and grid[rr - 1][rc] == 1:
                    grid[rr - 1][rc] = 2
                    rotten.append((rr - 1, rc))
                    f = 1
                if 0 <= rr + 1 <= tr - 1 and 0 <= rc <= tc - 1 and grid[rr + 1][rc] == 1:
                    grid[rr + 1][rc] = 2
                    rotten.append((rr + 1, rc))
                    f = 1
                if 0 <= rr <= tr - 1 and 0 <= rc - 1 <= tc - 1 and grid[rr][rc - 1] == 1:
                    grid[rr][rc - 1] = 2
                    rotten.append((rr, rc - 1))
                    f = 1
                if 0 <= rr <= tr - 1 and 0 <= rc + 1 <= tc - 1 and grid[rr][rc + 1] == 1:
                    grid[rr][rc + 1] = 2
                    rotten.append((rr, rc + 1))
                    f = 1

            if f == 1:  # any one good orange became rotten
                minutes = minutes + 1

        # if any unrotten even after while loop return -1
        for i in range(tr):
            for j in range(tc):
                if grid[i][j] == 1:
                    return -1

        # if all unrotten became rotten and did not return -1 then return minutes took to make them rotten
        return minutes
