class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Buckets, index i represents occurence of element
        bucket = [[] for i in range(len(nums) + 1)]
        # Count occurence
        hmap = {}
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        # Corresponding occurence with each number
        for num, occ in hmap.items():
            bucket[occ].append(num)
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res