class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()

        def dfs(ind, curr):
            if ind == len(nums):
                solution.append(curr[::])
                return
            
            curr.append(nums[ind])
            dfs(ind+1, curr)
            curr.pop()

            while ind + 1 < len(nums) and nums[ind] == nums[ind+1]:
                ind+=1
            dfs(ind + 1, curr)
        
        dfs(0, [])
        return solution
        