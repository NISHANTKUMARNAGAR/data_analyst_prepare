class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

a=ListNode(1)
b=ListNode(4)
c=ListNode(3)
d=ListNode(2)
e=ListNode(5)
f=ListNode(2)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
head=a

#Input:  head = [1, 4, 3, 2, 5, 2], x = 3
#Output: [1, 2, 2, 4, 3, 5]
t=3
curr=head
lowll=ListNode() #dummy low starting node
lower=lowll
highll=ListNode() #dummy high starting node
higher=highll
flag=0

while curr:
    if curr.val==t and flag==0: #if node==t store in pivot node
        temp=curr.next
        curr.next=None
        pivotnode=curr
        curr=temp
        flag=1
    elif curr.val<t: #if node.val<t join to lowll
        temp=curr.next
        curr.next=None
        lowll.next=curr
        lowll=lowll.next
        curr=temp
    elif curr.val>=t: #if node.val>t join to highll
        temp=curr.next
        curr.next=None
        highll.next=curr
        highll=highll.next
        curr=temp

if lower.next:
    tempcurr=lower.next #take 1st lower value in lowll in tempcurr
    while tempcurr.next:  #reach the end of this lowll
        if tempcurr.next is not None:
            tempcurr=tempcurr.next

    tempcurr.next=pivotnode #connect lowll end to pivotnode

pivotnode.next=higher.next #connect pivot node to highll after dummy node
printtemp=lower.next
while printtemp: #print all nodes in order
    print(printtemp.val)
    printtemp=printtemp.next