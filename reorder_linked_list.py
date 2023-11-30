# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# this uses fast pointer to find half of the linked list 
class Solution(object): # O(n), O(1)
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        # divide the linked list in half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # invert edges in second half
        curr = slow.next
        prev, slow.next = None, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        front, tail = head, prev
        # do the ordering
        while front and tail:
            tmp = front.next
            front.next = tail
            tmp2 = tail.next
            tail.next = tmp
            tail = tmp2
            front = tmp
