# removing nth node from end of ll
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        T=0
        curr=head #var to move from node to node
        while curr:
            curr=curr.next #here changing what current does not change head as we are reassigning curr not changing,curr.next or curr.val
                           #so doing this only changes curr not head's value
            T=T+1

        if(T==1): #if ll has just 1 node so no need to run below loops
            return None

        fromstart=(T-n)+1 #position of n from start
        temp=head #var to point to node being removed
        prevtemp=None #var to point to node just before the one being removed i.e. temp
        f=1 #temprory var to check if temp is at starting or not to adjust pointers
        while temp:
            fromstart=fromstart-1 #decreasing the counter till 0 i.e. reaching the node to be removed
            if(fromstart==0): #if reached the node to be removed
                if(f==1): #reaching the node to be removed is starting node
                    prevtemp=temp.next #taking and joining remaining list to prevtemp
                    return prevtemp #return remaining list
                else: #starting node is not to be removed, to remove some inner node in ll
                    prevtemp.next=temp.next #we can assign prevtemp.next something as this is when prevtemp is pointing to a node
                    return head
            else: #if not reached the node to be removed
                if(f==1): #if temp at starting node
                    prevtemp=temp
                    temp=temp.next
                    f=0
                else: #if temp is somewhere in middle of ll
                    prevtemp=prevtemp.next
                    temp=temp.next
"""

#removing node at pos location from start
"""class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

a=ListNode(10)
b=ListNode(20)
c=ListNode(30)
d=ListNode(40)
e=ListNode(50)

head=a
a.next=b
b.next=c
c.next=d
d.next=e

l = [10, 20, 30, 40, 50]
pos = 2
#remove node at pos 2 with 0 based indexing
#Output: [10, 20, 40, 50]

curr=head
prev=None
n=0
if head is not None: #it's not an empty list
    while curr:
        if pos==0: #if want to remove head
            temp=curr.next
            curr.next=None
            head=temp
        if n==pos and n!=0: #remove node at pos in 0 based indexing
            temp=curr.next
            curr.next=None
            curr=temp
            prev.next=curr
        else:
            prev=curr
            curr=curr.next
        n=n+1

curr=head
while curr:
    print(curr.val)
    curr=curr.next"""