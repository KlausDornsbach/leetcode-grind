import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) 
        while stones:
            if len(stones) == 1:
                break
            
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y != x:
                y -= x
                heapq.heappush(stones, y)
        
        if not stones:
            return 0
        
        return -stones[0]