# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.best = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recDiameter(node):
            if not node:
                return 0
            
            lLen = recDiameter(node.left)
            rLen = recDiameter(node.right)

            self.best = max(self.best, lLen + rLen)
            
            return 1 + max(lLen, rLen)

        recDiameter(root)
        return self.best