class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create maxHeap
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        # Choose remaining stone
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if second > first:
                heapq.heappush(maxHeap, first - second)
        
        if maxHeap:
            return abs(maxHeap[0])
        else:
            return 0