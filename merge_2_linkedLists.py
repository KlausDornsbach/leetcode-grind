# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        tail = head
        a, b = list1, list2

        while a and b:
            if a.val > b.val:
                tail.next = b
                b = b.next
            else:
                tail.next = a
                a = a.next
            
            tail = tail.next

        if a:
            tail.next = a
        
        if b:
            tail.next = b
        
        return head.next