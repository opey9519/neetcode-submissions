class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize 
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        # Pop from minHeap until there are k largest elements left
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        # Push val onto minHeap
        heapq.heappush(self.heap, val)
        # If there is more than k largest elements, pop
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Return the kth largest element
        return self.heap[0]
