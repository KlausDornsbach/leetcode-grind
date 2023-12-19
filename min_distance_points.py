import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            heap.append([dist, x, y])
        
        heapq.heapify(heap)
        sol = []
        while k:
            d, x, y = heapq.heappop(heap)
            sol.append([x, y])
            k-=1
        
        return sol