class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return

        def changetree(node, value):
            if node.left == None and node.right == None:
                if value is not None:  # if value is passed from parent of node
                    node.val = node.val + value
                return node.val

            if node.right:  # if right child exists go into it take passed value from parent and add returned value to current node
                rightval = changetree(node.right, value)
                node.val = node.val + rightval
            else:  # if no right child and value passed by parent is not None then add it to current node
                if value != None:
                    node.val = node.val + value

            if node.left:  # if left child exists then go into it take passed value and just return the returned value as its from left child so no add it to parent as we only add to parent value if its from right child
                leftval = changetree(node.left, node.val)
                return leftval
            else:  # if no left child just return current node value to parent
                return node.val

        changetree(root, None)
        return root

"""# HOW THIS APPROACH WORKS:
#
# 1. The main idea is to traverse the BST in reverse inorder (RIGHT -> ROOT -> LEFT).
#    Since larger values are present in the right subtree, processing it first allows
#    us to add all greater values to the current node.
#
# 2. The changetree(node, value) function receives the current node and a value
#    passed by its parent. This value represents the cumulative sum of previously
#    processed greater-valued nodes.
#
# 3. LEAF NODE CONDITION:
#    If both left and right children are None, the current node is a leaf.
#    If a value has been passed by the parent (value is not None), add it to the
#    current node. Otherwise, leave the node unchanged. Return the updated node
#    value because there are no more children to process.
#
# 4. PROCESSING THE RIGHT CHILD:
#    If a right child exists, recursively process it first and store its returned
#    cumulative value in rightval. Add rightval to the current node because the
#    returned value comes from the right subtree, which contains greater values.
#
# 5. IF THE RIGHT CHILD DOES NOT EXIST:
#    Enter the else branch. If the parent has passed a value, add that value
#    directly to the current node. If the passed value is None, do nothing.
#    This handles nodes that have no right subtree.
#
# 6. PROCESSING THE LEFT CHILD:
#    After updating the current node, check whether a left child exists.
#    If it does, recursively process it by passing node.val, which now contains
#    the current node's original value plus all greater values.
#
# 7. WHY WE DO NOT ADD THE RETURNED VALUE FROM THE LEFT CHILD:
#    The left subtree contains smaller values than the current node. Therefore,
#    its returned cumulative value must simply be passed further up without
#    being added to the current node. Adding it would incorrectly include
#    smaller values in the current node.
#
# 8. IF THE LEFT CHILD DOES NOT EXIST:
#    Enter the final else branch and return the current node's value directly.
#    This allows the updated cumulative value to propagate back to the parent.
#
# 9. WHY THE INITIAL VALUE IS NONE:
#    The first call is changetree(root, None) because the root has no parent
#    and no previously processed greater-valued nodes.
#
# 10. IMPORTANT THINGS TO REMEMBER:
#     - Reverse inorder traversal: RIGHT -> ROOT -> LEFT.
#     - Add the returned value when it comes from the RIGHT child.
#     - Never add the returned value when it comes from the LEFT child.
#     - Pass the updated current node value to the LEFT child.
#     - If a child does not exist, handle the situation using the corresponding
#       else branch.
#     - A leaf node simply adds the passed value, if one exists, and returns.
#
# TIME COMPLEXITY: O(n), because every node is visited exactly once.
# SPACE COMPLEXITY: O(h), due to the recursive call stack, where h is the
# height of the tree. In the worst case, it can be O(n)."""

#example working

"""
========================================================================================
FULL EXECUTION TRACE & BRANCH-COVERAGE EXAMPLE
========================================================================================

To trigger every single if/else branch in this implementation:
  1. Leaf with value is not None (adds value, returns node.val)
  2. Leaf with value is None     (leaves node.val as-is, returns node.val)
  3. node.right is True          (recurses right, adds rightval to node.val)
  4. node.right is False (else)  (checks if value != None, adds if present)
  5. node.left is True           (recurses left passing updated node.val, returns leftval)
  6. node.left is False (else)   (returns node.val directly to caller)

----------------------------------------------------------------------------------------
INPUT BST:
----------------------------------------------------------------------------------------
                        [ 5 ]
                       /     \
                    [ 2 ]   [ 8 ]
                   /     \
                [ 1 ]   [ 3 ]

- Node 8: Leaf with value == None (no parent sum yet).
- Node 5: Has right child (8) and left child (2).
- Node 2: Has right child (3) and left child (1).
- Node 3: Leaf with value != None (parent passed sum).
- Node 1: Leaf with value != None (parent passed sum).

----------------------------------------------------------------------------------------
STEP-BY-STEP RECURSIVE WALKTHROUGH:
----------------------------------------------------------------------------------------

1. INITIAL CALL:
   changetree(Node 5, value=None)
   - Not a leaf.
   - Branch: `if node.right:` -> True (Child is Node 8).
     Calls: changetree(Node 8, value=None)

2. CALL AT NODE 8:
   changetree(Node 8, value=None)
   - Branch: `if node.left == None and node.right == None:` -> True (Leaf).
   - Branch: `if value is not None:` -> False (value is None).
   - Leaf remains: 8.
   - Returns: 8.

3. RESUME AT NODE 5:
   - rightval = 8
   - node.val = 5 + 8 = 13.
   - Branch: `if node.left:` -> True (Child is Node 2).
     Calls: changetree(Node 2, value=13)

4. CALL AT NODE 2:
   changetree(Node 2, value=13)
   - Not a leaf.
   - Branch: `if node.right:` -> True (Child is Node 3).
     Calls: changetree(Node 3, value=13)

5. CALL AT NODE 3:
   changetree(Node 3, value=13)
   - Branch: `if node.left == None and node.right == None:` -> True (Leaf).
   - Branch: `if value is not None:` -> True (value is 13).
   - node.val = 3 + 13 = 16.
   - Returns: 16.

6. RESUME AT NODE 2:
   - rightval = 16
   - node.val = 2 + 16 = 18.
   - Branch: `if node.left:` -> True (Child is Node 1).
     Calls: changetree(Node 1, value=18)

7. CALL AT NODE 1:
   changetree(Node 1, value=18)
   - Branch: `if node.left == None and node.right == None:` -> True (Leaf).
   - Branch: `if value is not None:` -> True (value is 18).
   - node.val = 1 + 18 = 19.
   - Returns: 19.

8. RESUME AT NODE 2:
   - leftval = 19
   - Branch: `if node.left:` returned leftval (19).

9. RESUME AT NODE 5:
   - leftval = 19
   - Branch: `if node.left:` returned leftval (19).

----------------------------------------------------------------------------------------
FINAL GREATER TREE:
----------------------------------------------------------------------------------------
                       [ 13 ]
                       /     \
                   [ 18 ]   [ 8 ]
                   /     \
               [ 19 ]   [ 16 ]

----------------------------------------------------------------------------------------
NOTE ON UNVISITED 'ELSE' BRANCHES (NO LEFT / NO RIGHT CHILD):
----------------------------------------------------------------------------------------
If a node has ONLY a left child (e.g. Node 10 with left=7, right=None, passed value=15):
   - `if node.right:` is False -> enters `else:`
     - `if value != None:` -> node.val = 10 + 15 = 25.
   - Recurses into left child passing updated node.val (25).

If a node has ONLY a right child (e.g. Node 10 with left=None, right=14):
   - Recurses right, gets rightval (14), updates node.val = 10 + 14 = 24.
   - `if node.left:` is False -> enters `else:`
     - `return node.val` (returns 24 back to parent).
========================================================================================
"""