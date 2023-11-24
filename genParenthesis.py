class Solution(object):
    def generateParenthesis(self, n):
        def dfs(s, nopen, nclose):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if nopen < n:
                dfs(s + "(", nopen+1, nclose)
            
            if nclose < nopen:
                dfs(s + ")", nopen, nclose+1)
                
        res = []
        dfs("", 0, 0)

        return res