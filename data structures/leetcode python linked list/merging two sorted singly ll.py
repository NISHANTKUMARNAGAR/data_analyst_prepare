# merging two sorted linked list's
# (i) creating new final ll
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:  # if first ll empty
            return list2
        elif list2 is None:  # if second ll empty
            return list1
        elif (list1 is None) and (list2 is None):  # if both empty
            return []
        first = list1
        second = list2
        headoffinal = None
        final = None
        while first and second:  # till both list exists  i.e. non empty
            if (first.val > second.val):  # if second's value is smaller
                if (final == None):
                    final = ListNode(second.val,
                                     None)  # create new node in final ll if its empty with value of second's ll current node
                    headoffinal = final
                else:
                    final.next = ListNode(second.val,
                                          None)  # create new node in final ll if it already has a node with value of second's ll current node
                    final = final.next  # move final ll pointer to its next node
                second = second.next  # move seconds points to its next node
            elif (second.val > first.val):  # if first's value is smaller
                if (final == None):
                    final = ListNode(first.val,
                                     None)  # create new node in final ll if its empty with value of first's ll current node
                    headoffinal = final
                else:
                    final.next = ListNode(first.val,
                                          None)  # create new node in final ll if it already has a node with value of first's ll current node
                    final = final.next  # move final ll pointer to its next node
                first = first.next  # move first's points to its next node
            else:  # if both has same value we are taking first ll current node's value
                if (final == None):
                    final = ListNode(first.val, None)
                    headoffinal = final
                else:
                    final.next = ListNode(first.val, None)
                    final = final.next
                first = first.next

        if first is None:  # if first ll is processed fully add second's remaining values to final ll
            final.next = second
        elif second is None:  # if second ll is processed fully add first's remaining values to final ll
            final.next = first

        return headoffinal
"""
# (ii) using nodes of orignal sorted ll's
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: #if first ll empty
            return list2
        elif list2 is None: #if second ll empty
            return list1 
        first=list1
        second=list2
        headoffinal=None
        final=None
        while first and second: #till both list exists  i.e. non empty
            if(first.val>second.val): #if second's value is smaller
                if(final==None):
                    final=second #add second ll current node to final
                    #####final.next=None #setting final next pointer to none
                    headoffinal=final #getting pointer to first node of final ll
                else:
                    final.next=second #add second's ll current node to final next
                    final=final.next #move final ll pointer to its next node
                    #####final.next=None #setting final next pointer to none
                second=second.next #move seconds points to its next node
            elif(second.val>first.val): #if first's value is smaller
                if(final==None):
                    final=first #add first's ll current node to final
                    #####final.next=None #setting final next pointer to none
                    headoffinal=final #getting pointer to first node of final ll
                else:
                    final.next=first #add first's ll current node to final next
                    final=final.next #move final ll pointer to its next node
                    #####final.next=None #setting final next pointer to none
                first=first.next #move first's points to its next node
            else: #if both has same value we are taking first ll current node's value (code is same as above when first ll value's small)
                if(final==None):
                    final=first
                    #####final.next=None
                    headoffinal=final
                else:
                    final.next=first
                    final=final.next
                    #####final.next=None
                first=first.next

        if first is None: #if first ll is processed fully add second's remaining values to final ll
            final.next=second
        elif second is None: #if second ll is processed fully add first's remaining values to final ll
            final.next=first

        return headoffinal
        """
# important resons for ##### in (ii) in merging two sorted ll's
"""the main thing in this code is where ##### 5 hash are there we dont need to set .next to none for two reasons: 
1. as we rewrite the .next in every iteration so no need to put it to none and at the end we just point final
to remaing non empty list and that list's last node will be empty as input list1 and list2 would obviously have 
final node's next to None
2. the most important reason is as when do final=second or final=first we take put reference of that node to final
as these nodes are ListNode's objects these are not just values that we can copy we take reference of it not copy 
so if we do final.next=None we just lose remaining list of that ll,thats why we dont set it to None we just let 
it rewrite normally by loop"""