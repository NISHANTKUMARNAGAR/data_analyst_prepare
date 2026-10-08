#redundant connection
#O(nsquare)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots={} #stores node:root pair

        def pathcompression(node,minroot):
            for pair in roots:
                if roots[pair]==roots[node] and pair!=node: #same cluster
                    roots[pair]=minroot
            roots[node]=minroot

        for item in edges:
            if item[0] not in roots:
                roots[item[0]]=item[0]
            if item[1] not in roots:
                roots[item[1]]=item[1]
            if roots[item[0]]==roots[item[1]]: #same root i.e. cycle
                cyclepair=[item[0],item[1]]
            else:                            #different root union them
                minroot=min(roots[item[1]],roots[item[0]])
                if roots[item[0]]!=minroot:
                    pathcompression(item[0],minroot)
                if roots[item[1]]!=minroot:
                    pathcompression(item[1],minroot)

        return cyclepair

#less than before close to O(NlogN)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = {}

        def find(node):
            if roots[node] != node:
                roots[node] = find(roots[node])
            return roots[node]

        for item in edges:

            if item[0] not in roots:
                roots[item[0]] = item[0]

            if item[1] not in roots:
                roots[item[1]] = item[1]

            root1 = find(item[0])
            root2 = find(item[1])

            if root1 == root2:
                cyclepair = [item[0], item[1]]
            else:
                minroot = min(root1, root2)
                maxroot = max(root1, root2)

                roots[maxroot] = minroot

        return cyclepair