# this solution halves the time of the other (600ms to 300), maybe because we don't use another 
# function call internally every loop of the binary search, maybe because we are not using math
# import to calculate the ceiling of the division pile/sol, it also looks more elegant

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        # binary search through a brute force domain (cool af)
        mx = max(piles)
        l, r = 1, mx
        while l <= r:
            possible_sol = (l + r) // 2 
            tot_hours = 0
            for p in piles:
                tot_hours += p // possible_sol + (0 if p % possible_sol == 0 else 1)
            if tot_hours <= h:
                r = possible_sol - 1
            elif tot_hours > h:
                l = possible_sol + 1
        
        return l
        