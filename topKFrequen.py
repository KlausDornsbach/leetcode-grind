class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        return map(lambda x: x[0], sorted(d.items(), key=lambda x: x[1])[len(d.keys())-k:])
        