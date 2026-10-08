class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #finding out length of l1 and l2
        l1 = 0
        curr = headA
        while curr:
            curr = curr.next
            l1 = l1 + 1

        l2 = 0
        curr = headB
        while curr:
            curr = curr.next
            l2 = l2 + 1

        #we start comparing nodes when both have same number of nodes remaining and since
        #they if intersect join at some point so nodes after joining remain same and
        #we just have to make number of nodes same before joining so we find out large ll
        #do difference move that many nodes in larger ll now put pointer to smaller ll
        #now we from current pointer psoitions number of remaing nodes are same, we can
        #just go on comparing if they are same node or not using "is" which compares identity
        if (l1 > l2):
            #if 1st ll is larger
            temp = l1 - l2
            currA = headA
            for _ in range(temp):
                currA = currA.next

            currB = headB

        elif (l1 < l2):
            #if 2nd ll is smaller
            temp = l2 - l1
            currB = headB
            for _ in range(temp):
                currB = currB.next

            currA = headA

        elif (l1 == l2):
            #if same length,no need to move any pointer
            currA = headA
            currB = headB

        while currA:
            if currA is currB: #using "is" to check if same node or not
                return currA

            currA = currA.next
            currB = currB.next

        return None