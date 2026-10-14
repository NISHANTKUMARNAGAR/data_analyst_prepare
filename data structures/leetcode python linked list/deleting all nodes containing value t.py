class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

z=ListNode(6)
a=ListNode(1)
b=ListNode(2)
c=ListNode(6)
d=ListNode(3)
e=ListNode(4)
f=ListNode(5)
g=ListNode(6)

z.next=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g
head=z

#[6, 1, 2, 6, 3, 4, 5, 6]
#remove all nodes with value t
t = 6


curr=head
prev=None
while curr: #till node in curr
    if curr.val==t: #if node found
        temp=curr.next #store next node data
        curr.next=None #remove curr node from ll
        curr=temp #now next node is curr
        if prev: #if curr is not the 1st node
            prev.next=curr #and the prev points to curr thereby matched node removed
        elif prev==None: #we are at 1st node so removing it head should point to 2nd node that is curr
            head=curr
    else:
        prev=curr #if not found make curr node prev
        curr=curr.next #make next node curr

print("check")
curr=head
while curr:
    print(curr.val)
    curr=curr.next