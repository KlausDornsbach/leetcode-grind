# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object): # O(n), O(1)
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l, r = ListNode(None, head), head
        dist = 0
        
        while dist < n:
            r = r.next
            dist += 1
        
        while r:
            r = r.next
            l = l.next
    
        tmp = l.next.next
        l.next.next = None
        l.next = tmp

        if l.val == None:
            return l.next
        
        return head
