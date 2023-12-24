# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        copied = dict()

        def dfs(node: Optional['Node']):
            if node.val in copied:
                return copied[node.val]
            
            copy = Node(node.val, None)
            copied[copy.val] = copy
            
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node)

