import heapq


class Solution:
    def maxEvents(self, A: List[List[int]]) -> int:
        A.sort(reverse=1)
        h = []
        res = d = 0
        while A or h:
            if not h: d = A[-1][0]
            while A and A[-1][0] <= d:
                heapq.heappush(h, A.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res