#using python list O(n) time and space
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head.next==None):
            return True
        curr=head
        temp=[]
        while curr:
            temp.append(curr.val)
            curr=curr.next

        if(temp==list(reversed(temp))):
            return True
        else:
            return False
"""

#by reversing half of ll then compare O(n) time ,O(1) space
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head.next==None): #if length is 1
            return True

        #to find either middle or 2nd middle
        fast=head
        slow=head
        prevslow=None #node jjust before middle(slow) to join reversed linked list to
        while fast and fast.next:
            prevslow=slow
            slow=slow.next
            fast=fast.next.next

        #prevslow will be the node we join reversed list to
        #if fast==None,slow at 2nd middle i.e. where we need to reverse the ll from
        #if fast!=None,slow is at middle nodes,i.e. we need to reverse nodes from just after middle to last
        if(fast==None): #even
            curr=slow
        elif(fast!=None):#odd
            curr=slow.next
        prev=None
        while curr:#to reverse the ll from middle to end
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        prevslow.next=prev #joining end to node just before middle

        #now to check if palindrome we need to compare from head to middle and middle to end
        #as we reversed from middle to end if palindrome should have same vales as from head to middle
        #if any where value is not same we stop and declare not palindrome
        palinchkmid=prev
        while palinchkmid:
            if(head.val!=palinchkmid.val):
                return False
            head=head.next
            palinchkmid=palinchkmid.next
        
        #if not palindrome while retruns false,if its while ends normally when palinchkmid reaches none
        #after last comparision we return True
        return True
"""