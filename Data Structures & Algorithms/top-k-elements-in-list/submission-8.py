class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create n number of buckets: n = len(nums)
        bucket = [[] for i in range(len(nums) + 1)]
        # Track num occurences
        hmap = {}
        # Count num occurences
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        # Place num into occured bucket
        for num, occured in hmap.items():
            bucket[occured].append(num)

        count_frequent = []

        # Scan each item in each bucket until found k most frequent
        for b in range(len(bucket) -1, -1, -1):
            for v in bucket[b]:
                count_frequent.append(v)
                if len(count_frequent) == k:
                    return count_frequent