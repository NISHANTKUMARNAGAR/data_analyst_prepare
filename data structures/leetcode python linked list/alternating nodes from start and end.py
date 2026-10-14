#works for both even,odd,zero and one length ll
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)
f=ListNode(6)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
head=a


#Input:  [1, 2, 3, 4, 5, 6]
#Output: [1, 6, 2, 5, 3, 4]
#take 1 node from front one from back and again and again

#step 1 reaching halfway point
slow=head
fast=slow.next
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next

#reverse from slow.next i.e. from 4 to end i.e. 6 to 6,5,4
#and 4 to none and 3 to 6 later so we would have 1,2,3,6,5,4
curr=slow.next #i.e. 4
prev=None
while curr:
    temp=curr.next
    curr.next=prev
    prev=curr
    curr=temp

#this means we have 6->5->4->None
#now we separate initial  half and last half
slow.next=None #i.e. 3->None in 1->2->3->None
#now we have 1->2->3->None, 6->5->4->None

#now we need to start from head i.e. 1 and prev i.e. 6 taking alternate like 1,6,2,5,3,4
fromstart=head
fromlast=prev
while fromstart and fromlast:
    fromstartnext=fromstart.next #2 stored in fromstartnext
    fromstart.next=fromlast #fromstart 1 points to 6
    fromlastnext=fromlast.next #5 stored in fromlastnext
    fromlast.next=fromstartnext  #fromlast 6 points to 2 so we have 1->6->2
    fromstart=fromstartnext #i.e. new fromstart is 2
    fromlast=fromlastnext #i.e. new fromlast is 5


#print all 1->6->2->5->3->4
pcurr=head
while pcurr:
    print(pcurr.val)
    pcurr=pcurr.next