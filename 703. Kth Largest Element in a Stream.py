class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums,k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        if self.minHeap and val <= self.minHeap[0] and len(self.minHeap) >= self.k:
            return self.minHeap[0]
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
