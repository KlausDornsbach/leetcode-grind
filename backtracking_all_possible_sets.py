import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        curr_set = []

        def dfs(idx):
            if idx >= len(nums):
                ret.append(copy.deepcopy(curr_set))
                return
          
            curr_set.append(nums[idx])

            # either you want to append the next
            dfs(idx + 1)

            # or you don't
            curr_set.pop()
            dfs(idx + 1)
            return
        
        dfs(0)
        return ret