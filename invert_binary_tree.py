# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object): #O(n) O(n) (recursive stack space)
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def recursiveInvert(node):
            if not node:
                return
            tmp = node.left
            node.left = node.right
            node.right = tmp
            recursiveInvert(node.left)
            recursiveInvert(node.right)
        
        recursiveInvert(root)
        return root