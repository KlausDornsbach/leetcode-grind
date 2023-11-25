class Solution(object):
    def twoSum(self, numbers, target): # worse solution but generalized
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(numbers)):
            d[numbers[i]] = i
        for i in range(len(numbers)):
            if target - numbers[i] in d:
                return [i+1, d[target - numbers[i]]+1]