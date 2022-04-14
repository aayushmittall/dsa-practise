class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first == second:
                pass
            else:
                element = first - second
                heapq.heappush(stones,element)
        return -1*stones[0] if stones else 0
