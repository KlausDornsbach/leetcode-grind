
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    # single pass solution 
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = {None: None} # have a reference to every element
        
        curr = head
        while curr:
            if curr not in dic: # create new node
                dic[curr] = Node(curr.val)
            
            curr_new = dic[curr]
            # if the node was already created from other point
            # and the value was not added yet
            if curr_new.val == -10001: 
                curr_new.val = curr.val
            # add the random node
            if curr.random not in dic:
                dic[curr.random] = Node(-10001)
            curr_new.random = dic[curr.random]
            
            # add the next node
            if curr.next not in dic:
                dic[curr.next] = Node(-10001)
            curr_new.next = dic[curr.next]

            # next
            curr = curr.next

        return dic[head]
    
    # this solution is way better, because although it passes 2 times through the 
    # whole list, it performs way less operations in each iteration (also more 
    # elegant)
    def copyRandomList2(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = {None: None}
        curr = head
        while curr:
            newNode = Node(curr.val)
            dic[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            dic[curr].next = dic[curr.next]
            dic[curr].random = dic[curr.random]
            curr = curr.next
        
        return dic[head]
            