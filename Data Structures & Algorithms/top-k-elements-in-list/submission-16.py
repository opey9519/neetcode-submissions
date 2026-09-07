class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        hmap = {}

        # Track occurence
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        
        # Slot each value in its occurence bucket
        for num, occ in hmap.items():
            bucket[occ].append(num)
        
        res = []
        # [[], [1], [2], [3], [], [], []]
        # k = 2
        for i in range(len(bucket) - 1, -1, -1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        

        
