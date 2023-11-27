class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            q = (l + r)//2
            if nums[q] == target:
                return q
            elif nums[q] < target:
                l = q + 1
            else:
                r = q - 1
        
        return -1