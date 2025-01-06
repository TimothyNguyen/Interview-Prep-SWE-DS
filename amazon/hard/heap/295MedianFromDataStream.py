'''
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of 
the actual answer will be accepted.

addNum()/findMedian():
- Time: O(log n)
Space: O(n)
'''

import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)  # Push negative to simulate max-heap
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == 0:
            return 0
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
