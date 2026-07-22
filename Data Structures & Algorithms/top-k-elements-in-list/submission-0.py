class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-val, key) for key, val in count.items()]
        heapq.heapify(heap)
        res = []
        while k>0:
            value, key = heapq.heappop(heap)
            res.append(key)
            k -=1
        return res

        