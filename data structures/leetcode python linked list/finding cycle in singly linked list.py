#finding cycle in ll
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None):#if no node exists,no loop
            return False
        elif(head.next==None):#only one node exists,no loop possible
            return False
        fast=head
        slow=head
        temp=1 #to skip when they are initially the same i.e. fast=slow=head
        while fast and fast.next: #to check if cycle exists
            #if cycle exists fast and slow will become same besides when they are same at start of while
            #because of cycle in loop and we return True
            if(fast==slow): #if they become same
                if(temp==1): #if same when they are both head wew skip that we are to check after ini. position
                    temp=0 #so we dont this case or if again
                else: #if same but other than initial head,meaning cycle exists so return true
                    return True
            slow=slow.next
            fast=fast.next.next
        #if in while loop or cycle does not exist,while ends we return false
        return False
"""
#improvised method to skip initial same head position check
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None):#if no node exists,no loop
            return False
        elif(head.next==None):#only one node exists,no loop possible
            return False
        fast=head
        slow=head
        while fast and fast.next: #to check if cycle exists
            #if cycle exists fast and slow will become same besides when they are same at start of while
            #because of cycle in loop and we return True
            slow=slow.next
            fast=fast.next.next
            if(fast==slow): #if they become same
                return True
        #if in while loop or cycle does not exist,while ends we return false
        return False
"""
#we just moved pointer first then we checked so that skip over initial check when both are head
#so we move pointer first then we check