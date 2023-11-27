import math

# this solution is crap (beats 5% on time and 27% on memory) 
# we use binary search on the domain of possible brute force solutions
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        def test_possibility(pos):
            tot_hours = 0
            print(pos)
            for p in piles:
                tot_hours += math.ceil(float(p)/float(pos))
            return tot_hours
        # binary search through a brute force domain (cool af)
        mx = max(piles)
        l, r, best_sol = 1, mx, mx # initialize best solution to be the max
        while l <= r:
            possible_sol = (l + r) // 2 
            tot_hours = test_possibility(possible_sol)
            if tot_hours <= h:
                if possible_sol < best_sol:
                    best_sol = possible_sol
                r = possible_sol - 1
            elif tot_hours > h:
                l = possible_sol + 1
        
        return best_sol
        