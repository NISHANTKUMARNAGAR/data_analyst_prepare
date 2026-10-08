# finding middle(odd) or secondmiddle(even) of singly linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #using two pointer to find middle
        #first moves one by one while moves twice as fast and at end,first will be at middle(odd),close to it(even no. of nodes)
        #initially both start at head
        first=head
        second=head
        #here in ll,head is not some seperate node its just a pointer to 1st node ie. head=1st node or head.next is actually 1st node.next
        while second and second.next:
            #we check both second and its next as if second is none, its next will give error
            #and also .next might be none so we also need to check it so that we dont acess second.next.next in loop
            first=first.next
            second=second.next.next

        return first
        #for both even and odd numbered linked list,fp ends up at either exactly middle or at 2nd middle for even numbered
"""