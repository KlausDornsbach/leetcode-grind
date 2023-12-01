# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def recursionMaxDepth(node, currdepth):
            if not node:
                return currdepth

            currdepth+= 1
            
            dl = recursionMaxDepth(node.left, currdepth)
            dr = recursionMaxDepth(node.right, currdepth)
            return max(dl, dr)
        
        return recursionMaxDepth(root, 0)