#reversal of singly linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  # as head is initial pointer to linked list thats why we start from there
        previous = None  # head has no previous node, also we use this to make current node point to previous node
        while current:  # we use while as not knowing how many nodes and till current as we stop after last node as then curr will be None
            next_node = current.next  # storing next of current before making any changes as we will lose remaining list if we alter first
            current.next = previous  # making currnet node to point to previous node i.e. reversing it
            # now we change previous,current as we change iterables like i in normal array to point  prev to curr node,curr. to next node
            previous = current  # we make curr. as prev. as for next node this becomes prev. node(prev. assigned first as if we change curr first we lose the curr node)
            current = next_node  # now the next node becomes curr like we do i=i+1 in case of array

        return previous  # at last we return previous as while stops when curr is None i.e. previous has last node or 1st node of reversed linked list
"""