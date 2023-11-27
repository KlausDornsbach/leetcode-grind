class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        t = 0
        b = len(matrix) - 1
        while t <= b:
            i = (t + b)//2
            if matrix[i][0] <= target <= matrix[i][-1]:
                l = 0
                r = len(matrix[0]) - 1
                while l <= r:
                    already_tried = True
                    j = (l + r)//2
                    if matrix[i][j] == target:
                        return True
                    elif matrix[i][j] < target:
                        l = j+1
                    else:
                        r = j-1

                return False
            
            if matrix[i][0] > target:
                b = i-1
            
            if matrix[i][-1] < target:
                t = i+1
                
        return False