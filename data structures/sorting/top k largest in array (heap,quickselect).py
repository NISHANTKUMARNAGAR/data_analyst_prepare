#using heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        from heapq import heappop, heappush
        heap = []
        for item in nums:
            heappush(heap, -item)

        while k != 1:  # remove till kth element comes on top i.e. heap[0]
            heappop(heap)
            k = k - 1

        return -heap[0]

#using quickselect
