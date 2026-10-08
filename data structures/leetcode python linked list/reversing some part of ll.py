# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if (head.next == None):  # only one node no reversal
            return head
        if (left == right):  # if left==right no need to reverse ex.[3,5] left=right=1 no change
            return head
        f = 0  # integer to move through linked list
        curr = head
        prev = None
        beforeleft = None
        if (left < right):
            while f < right + 1:  # to work till we cross right numbered node location
                f = f + 1
                if (f == left - 1):  # to store node before left numbered node
                    beforeleft = curr
                    curr = curr.next
                elif (f < left):  # to move through linked list by moving curr
                    curr = curr.next
                elif f <= right and f >= left:  # to reverse the list from left numbered node to right numbered node
                    if (f == left):  # if node is left store it will be used later to join reversed list to orignal
                        leftnode = curr
                    nextnode = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextnode

            leftnode.next = curr  # to join left numbered node to node after right numbered node
            # works for both cases if right of right numberd node is None or not
            if beforeleft:  # i.e. left is after head location
                beforeleft.next = prev  # to join before left node to right numbered node i.e.  in l=[1,2,3,4,5]  left=2 and right=4 join 1 to 4
                return head
            else:  # if left is head i.e. ex=[1,2,3] left is 1 regardless of right value
                return prev