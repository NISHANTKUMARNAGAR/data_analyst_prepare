#tree structure leetcode behind the scences
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#find max depth of tree(my way goes down inc. depth and return max depth from left,right subtree):-------
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def finddepth(node):
            ld,rd=0,0 #incase if left and right subtree are null
            if node.left:
                ld=finddepth(node.left)
            if node.right:
                rd=finddepth(node.right)
            return max(ld,rd)+1 #we take max of ld,rd  also inc. 1 to count this node

        maxd=0
        if root:
            maxd=finddepth(root) #root has 1 depth by default if it exists
        return maxd

#find if its same tree or not meaing the nodes and their values are same or not:---------
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None: #if both empty hence same
            return True
        elif p==None or q==None: #if anyone None hence not same
            return False
        else:
            #bith exist and are non empty
            if p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
            else:
                return False

#invert binary tree:------------
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def task(node):
            # dont care if node's left or right is null or not just swap them
            node.left, node.right = node.right, node.left

            if node.left:
                task(node.left)
            if node.right:
                task(node.right)

        if root:
            task(root)

        return root

#level order traversal,left to right:---------
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        def gen(node, d):
            answer[d].append(node.val)
            if (node.left or node.right) and len(answer) == d + 1:
                #if no new place for child nodes exist in answer list create new inner list
                answer.append([])
            if node.left:
                gen(node.left, d + 1)
            if node.right:
                gen(node.right, d + 1)

        if root:
            answer.append([])
            gen(root, 0)

        return answer

#validate binary search tree:---------
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, ul, ll):
            if (ul != None and node.val >= ul) or (ll != None and node.val <= ll):
                return False

            #keep parents ul,ll and use in children wherever necesarry and dont mix ul,ll in siblings
            parentul = ul
            parentll = ll
            if (node.left and check(node.left, ul := node.val, parentll) == False) or (
                    node.right and check(node.right, parentul, ll := node.val) == False):
                # recursive call for left and right subtree
                return False

        if root:
            if check(root, None, None) is None:
                return True
            else:
                return False

#find lowest common ancestor of two nodes:--------
#lowest common ancestor is common ancestor and a node can be ancestor of itself
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathp = []
        pathq = []

        def findpath(node, path, tofind):
            if node == tofind:  # backtracking condition
                return node

            # using backtracking,dfs to find node in binary tree
            if node.left:
                path.append(node.left)  # make choice
                if findpath(node.left, path, tofind):  # backtracking recursion
                    return path
                path.pop()  # undo choice if not found
            if node.right:
                path.append(node.right)
                if findpath(node.right, path, tofind):
                    return path
                path.pop()
            # we specifically using this if-else because a binarytree has either left or right subtree

        # to find paths for p and q nodes
        pathp.append(root)
        findpath(root, pathp, p)
        pathq.append(root)
        findpath(root, pathq, q)

        # to find the lca(lowest common ancestor)
        common = []
        i = 0
        while True:
            if i != len(pathp) and i != len(pathq) and pathp[i] == pathq[i]:
                common.append(pathp[i])  # find common path and return last common node
            else:
                return common[-1]  # lca
            i = i + 1