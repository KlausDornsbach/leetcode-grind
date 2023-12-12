class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        curr = []
        dic = dict(map(lambda x: (x, 0), nums))

        def dfs(i):
            if i >= len(nums):
                sol.append(curr.copy())
                return
            
            for k, v in dic.items():
                if v == 0:
                    dic[k] = 1
                    curr.append(k)
                    dfs(i+1)
                    dic[k] = 0
                    curr.pop()
        
        dfs(0)
        return sol
