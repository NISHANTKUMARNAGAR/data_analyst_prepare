# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:

        def trace(node,n,d):
            if node.left is None and node.right is None:
                return n

            ln,rn=0,0
            if node is root: #if current is root node
                if node.left: ln=trace(node.left,n+1,"left")
                if node.right: rn=trace(node.right,n+1,"right")
            else: #if any other node
                if node.left and d=="right": #if earlier direction was right and want to got to left continue earlier path
                    ln=trace(node.left,n+1,"left")
                if node.left and d=="left": #if earlier direction was left and want to go towards left start again from 1
                    ln=trace(node.left,1,"left")
                if node.right and d=="left": #if earlier direction was left and want to go towards right continue earlier path
                    rn=trace(node.right,n+1,"right")
                if node.right and d=="right": #if earlier direction was right and want to go towards right start again from 1
                    rn=trace(node.right,1,"right")

            return max(ln,rn,n) #compare lengths from both subtrees left and right with current length

        return trace(root,0,None)

"""
LeetCode 1372: Longest ZigZag Path in a Binary Tree

This problem asks us to find the longest ZigZag path anywhere in a binary tree. A ZigZag path is a path in which every consecutive edge alternates direction: left, right, left, right, or right, left, right, left. The path can start at any node, not just the root, and its length is measured in EDGES, not nodes.

APPROACH: RECURSION WITH DIRECTION AND PATH LENGTH

The helper function trace(node, n, d) uses three pieces of information:
- node: the current node being explored.
- n: the length of the current ZigZag path in edges.
- d: the direction used to reach the current node ("left" or "right"). At the root, d is None because there is no previous direction.

The key idea is to explore both children of every node while tracking the current ZigZag length. If the next move is in the opposite direction from the previous move, the ZigZag continues, so we increase n by 1. If the next move is in the same direction, the ZigZag is broken, so we start a new path with length 1 using that edge.

For example, if the previous move was left:
- Moving right continues the ZigZag, so the new length is n + 1.
- Moving left breaks the ZigZag, so the new length is 1.

Similarly, if the previous move was right:
- Moving left continues the ZigZag, so the new length is n + 1.
- Moving right breaks the ZigZag, so the new length is 1.

At the root, there is no previous direction to compare. Therefore, the code explores both the left and right children, starting each path with length 1 because each move represents one edge.

BASE CASE:
When the current node is a leaf (both children are None), the path cannot continue. The function returns n, the length accumulated along the current path.

TRACKING THE BEST ANSWER:
The variables ln and rn store the best ZigZag lengths returned by the recursive calls through the left and right children, respectively. The expression max(ln, rn, n) compares the best results from both subtrees with the current path length n.

This comparison is important because the longest ZigZag path may end at the current node or occur deeper inside either subtree. We must preserve the best result found anywhere in the tree, even when the current ZigZag is broken and a new one starts.

THREE IMPORTANT THINGS TO REMEMBER:
1. n counts EDGES, not nodes. The first move from the root gives a length of 1.
2. d remembers the previous direction. An opposite direction extends the path with n + 1, while the same direction resets the new path to 1.
3. max(ln, rn, n) ensures that the longest path found anywhere in the tree is not lost while recursion explores other branches.

IMPORTANT EDGE CASE:
The code assumes root is not None. To handle an empty tree safely, add `if root is None: return 0` at the beginning of longestZigZag. A single-node tree has no edges, so its answer is 0.

COMPLEXITY:
Time: O(N), where N is the number of nodes, because each node is visited once.
Auxiliary space: O(H), where H is the height of the tree, due to the recursive call stack. In the worst case of a completely skewed tree, H can be N.

MAIN LESSON:
This is a tree recursion problem where each recursive call carries information about the path so far. The direction tells us whether the current path can continue, the length tracks its progress, and the returned maximum preserves the best answer found across the entire tree.
"""