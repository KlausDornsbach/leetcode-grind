class Solution(object): # cpu:O(log(n)), mem:O(1)
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        smol = nums[0]
        while l <= r:
            m = (l + r)/2
            if nums[m] < smol:
                smol = nums[m]

            if nums[r] <= nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return smol