#Course Schedule I check if courses can be done---------------------------------------------
#using list
#time complexity O(V*E),,V=no. of nodes,,E=no. of edges
#means if each time in while only one node has indegree 0 then while runs V times and inside it
#for loop over prerequisites runs E times each time so O(V*E) time complexity in worst case
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 or numCourses == 0:
            return True

        zero = set()  # nodes with zero indegree
        nonzero = set()  # nodes with non zero indegree
        while True:
            if len(prerequisites) == 0:  # no cycle
                return True

            for i in range(len(prerequisites)):
                if prerequisites[i][0] == prerequisites[i][1]:  # a to a dependency will not do
                    return False
                if prerequisites[i][0] in zero:  # about the non zero indegree or dependent one
                    zero.remove(prerequisites[i][0])
                nonzero.add(prerequisites[i][0])
                if prerequisites[i][1] not in nonzero:  # node with zero indegree currently
                    zero.add(prerequisites[i][1])

            if len(zero) == 0:  # if zero indegree then definitely a cycle
                return False

            newprerequisites = []
            for i in range(len(prerequisites)):  # remove all node with zero indegree
                if prerequisites[i][1] not in zero:
                    newprerequisites.append(prerequisites[i])

            prerequisites = newprerequisites.copy()
            zero.clear()
            nonzero.clear()

#using adjacency list=used to store edges in graph but non-weighted graph so store like---------
#dictionary[node]=[nodes which key node points to]
#using queue to store zero indegree nodes
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 or numCourses == 0:
            return True

        from collections import deque
        zero = deque()  # nodes with zero indegree #collections deque
        indegree = {}  # dictionary to store nodes and their indegree
        edges = {}  # dictionary to store edges #adjacency list

        for i in range(len(prerequisites)):  # find and store indegree of all
            # store edge in 'edges'
            if prerequisites[i][1] not in edges:
                edges[prerequisites[i][1]] = [prerequisites[i][0]]
            else:
                edges[prerequisites[i][1]].append(prerequisites[i][0])

            # store indegree in indegree
            if prerequisites[i][1] not in indegree:
                indegree[prerequisites[i][1]] = 0
            if prerequisites[i][0] not in indegree:
                indegree[prerequisites[i][0]] = 1
            else:
                indegree[prerequisites[i][0]] = indegree[prerequisites[i][0]] + 1

        for item in indegree:  # put all zero indegree items in zero deque
            if indegree[item] == 0:
                zero.append(item)

        while len(zero) != 0:
            current = zero.popleft()  # taking current node with zero indegree
            if current in edges:
                for item in edges[current]:  # for each node current is connected to
                    indegree[item] = indegree[item] - 1  # decrement indegree
                    if indegree[item] == 0:  # if reached 0 indegree add to zero deque
                        zero.append(item)

            # repeat till zero is empty means no node with zero indegree i.e. a cycle

        # if that while loop completed sucessfully then all nodes processed
        for item in indegree:  # to check if a cycle
            if indegree[item] != 0:  # if any node's indegree is not 0 at end
                print(item)
                return False

        return True  # if before for loop completes sucessfully all indegree 0 so no cycle

#Course Schedule II return ordering on how to complete courses----------------------------------
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        from collections import deque
        zero = deque()  # nodes with zero indegree #collections deque
        indegree = {}  # dictionary to store nodes and their indegree
        edges = {}  # dictionary to store edges #adjacency list
        doneCourses = []

        for i in range(len(prerequisites)):  # find and store indegree of all
            # store edge in 'edges'
            if prerequisites[i][1] not in edges:
                edges[prerequisites[i][1]] = [prerequisites[i][0]]
            else:
                edges[prerequisites[i][1]].append(prerequisites[i][0])

            # store indegree in indegree
            if prerequisites[i][1] not in indegree:
                indegree[prerequisites[i][1]] = 0
            if prerequisites[i][0] not in indegree:
                indegree[prerequisites[i][0]] = 1
            else:
                indegree[prerequisites[i][0]] = indegree[prerequisites[i][0]] + 1

        for i in range(numCourses):
            # adding courses which re not in prerequisite i.e. courses which are allowed
            # to be completed without any dependency
            if i not in indegree:
                doneCourses.append(i)

        for item in indegree:  # put all zero indegree items in zero deque
            if indegree[item] == 0:
                zero.append(item)

        while len(zero) != 0:
            current = zero.popleft()  # taking current node with zero indegree
            doneCourses.append(current)
            if current in edges:
                for item in edges[current]:  # for each node current is connected to
                    indegree[item] = indegree[item] - 1  # decrement indegree
                    if indegree[item] == 0:  # if reached 0 indegree add to zero deque
                        zero.append(item)

            # repeat till zero is empty means no node with zero indegree i.e. a cycle

        # if that while loop completed sucessfully then all nodes processed
        if len(doneCourses) == numCourses:
            return doneCourses
        else:
            return []