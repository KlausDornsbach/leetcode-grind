# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        
        def rec(prev, curr):
            
            if not curr:
                return prev
            
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            return rec(prev, curr)

        return rec(None, head)