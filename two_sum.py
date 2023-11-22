class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(0, len(nums)):
            d[nums[i]] = i
        
        for i in range(0, len(nums)):
            r = target - nums[i]
            if r in d and i != d[r]:
                return [i, d[r]]
