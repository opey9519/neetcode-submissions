class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            # maintain heap length of k
            if len(heap) > k:
                heapq.heappop(heap)
        
        # if 3 elements, len(heap) = 3, since minheap we return top (3rd largest)
        return heap[0]