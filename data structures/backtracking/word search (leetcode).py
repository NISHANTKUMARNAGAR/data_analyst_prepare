class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # if character freq in word must be equal or less than that in board then only we do any checking
        flag = True
        from collections import Counter
        flattenboard = [e for row in board for e in row]
        cb = Counter(flattenboard)
        cw = Counter(word)
        for worditem in cw:
            if cw[worditem] > cb[worditem]:  # if any required item is not in sufficient value in board no need to check
                return False

        colbound = len(board)  # bound for y
        rowbound = len(board[0])  # bound for x
        seencell = set()

        def findword(respoint, py, px, currword):  # backtracking function
            if len(currword) == len(word):  # result case
                return True

            if -1<py<colbound and -1<px-1<rowbound and (py,px-1) not in seencell and board[py][px-1]: #left letter
                if board[py][px - 1] == word[respoint]:
                    seencell.add((py, px - 1))
                    currword.append(board[py][px - 1])
                    if findword(respoint + 1, py, px - 1, currword):
                        return True
                    currword.pop()
                    seencell.remove((py, px - 1))

            if -1<py<colbound and -1<px+1<rowbound and (py,px+1) not in seencell and board[py][px+1]: #right letter
                if board[py][px + 1] == word[respoint]:
                    seencell.add((py, px + 1))
                    currword.append(board[py][px + 1])
                    if findword(respoint + 1, py, px + 1, currword):
                        return True
                    currword.pop()
                    seencell.remove((py, px + 1))

            if -1<py-1<colbound and -1<px<rowbound and (py-1,px) not in seencell and board[py-1][px]: #upper letter
                if board[py - 1][px] == word[respoint]:
                    seencell.add((py - 1, px))
                    currword.append(board[py - 1][px])
                    if findword(respoint + 1, py - 1, px, currword):
                        return True
                    currword.pop()
                    seencell.remove((py - 1, px))

            if -1<py+1<colbound and -1<px<rowbound and (py+1,px) not in seencell and board[py+1][px]: #lower letter
                if board[py + 1][px] == word[respoint]:
                    seencell.add((py + 1, px))
                    currword.append(board[py + 1][px])
                    if findword(respoint + 1, py + 1, px, currword):
                        return True
                    currword.pop()
                    seencell.remove((py + 1, px))

        def checkeverychar():  # check all in grid
            for y in range(len(board)):
                row = board[y]
                for x in range(len(row)):
                    if word[0] == board[y][x]:
                        seencell.add((y, x))
                        if findword(1, y, x, [board[y][x]]):
                            return True
                        seencell.remove((y, x))

        if checkeverychar():
            return True
        else:
            return False

s=Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))

"""
WORD SEARCH — BACKTRACKING REVISION NOTES

PROBLEM:
Given a 2D character grid and a target word, determine whether the
word can be formed by moving horizontally or vertically between
adjacent cells. The same cell cannot be used more than once in a
single path. Return True if a valid path exists, otherwise False.

1. COUNTER PREPROCESSING:
- Flatten the board into a single list using a nested list comprehension
  so that every character in every row is collected.
- Counter(flattenboard) gives the frequency of each character in the
  entire board. Counter(word) gives the frequency required by the word.
- If the word requires a character more times than the board contains,
  return False immediately. No path can possibly form the word.
- This is an early-rejection optimisation; matching frequencies alone
  does not guarantee that a valid adjacent path exists.

2. BOUNDARIES AND STATE:
- colbound = len(board) gives the number of rows (the y boundary).
- rowbound = len(board[0]) gives the number of columns (the x boundary).
- seencell is a set of (row, column) coordinates already used in the
  current path. A set makes membership checks efficient and prevents
  revisiting a cell within the same word path.
- currword stores the characters currently collected along the path.
- respoint is the index of the next character to match in word.
- py and px represent the current cell's row and column.

3. THE OUTER DOUBLE LOOP — checkeverychar():
- The nested loops visit every cell in the board because the word can
  begin at any location.
- Only cells matching word[0] are considered as starting points.
- The starting coordinate is added to seencell, then findword() is
  called with respoint = 1 because the first character is already
  matched and stored in currword.
- If findword() returns True, checkeverychar() immediately returns True.
- If that starting point fails, its coordinate is removed from
  seencell so another starting point can be tried independently.
- If every possible starting point fails, the function returns None,
  which is falsy; the outer method consequently returns False.

4. THE BACKTRACKING FUNCTION — findword():
- The base case checks whether len(currword) == len(word). If so,
  every character has been matched, so it returns True.
- Otherwise, it tries the four possible directions: left, right, up
  and down.
- Each direction first checks that the coordinate is inside the board,
  that the cell has not already been used, and that the cell contains
  a truthy character.
- It then checks whether the neighbour matches word[respoint].
- A matching neighbour is added to seencell and its character is
  appended to currword before the recursive call.
- The recursive call advances respoint by one and moves the current
  position to that neighbour.
- If the recursive call returns True, True is immediately propagated
  through every active recursive call. The successful path is retained
  and no further directions or starting points need to be checked.

5. WHY BACKTRACKING IS NECESSARY:
- A matching neighbour may lead to a dead end later. Finding one
  matching character does not guarantee the remaining word can be made.
- If a recursive call fails, currword.pop() removes the last character
  and seencell.remove() releases the coordinate.
- These undo operations restore the previous state so another direction
  can be explored without being affected by the failed path.
- Each branch therefore explores a different possible path while
  respecting the rule that a cell cannot be reused within that path.
- If all four directions fail, findword() reaches the end without
  returning True, so it returns None (falsy). The caller then undoes
  its choice and tries another direction.

6. HOW THE FINAL RESULT IS DECIDED:
- If any starting point produces a complete valid path, True travels
  back through the recursive calls and the method returns True.
- If every starting point and every possible path fails, no call
  finds a complete word. checkeverychar() returns None, and the final
  if/else returns False.

IMPORTANT:
The set tracks coordinates, not characters. Two different cells may
contain the same character and both can be used in one path, provided
they are different coordinates. The Counter check only rejects
impossible character frequencies; adjacency and cell reuse are handled
by the backtracking search.
"""