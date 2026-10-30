# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        n = 1  # as root is always good

        def findgood(node, currmax):
            nonlocal n
            if node is not root and node.val >= currmax:  # we check if current is greatest so far so nodes before had =/< values
                currmax = node.val
                n = n + 1

            if node.left:
                findgood(node.left, currmax)
            if node.right:
                findgood(node.right, currmax)

        findgood(root, root.val)  # current node,current maximum valued node
        return n