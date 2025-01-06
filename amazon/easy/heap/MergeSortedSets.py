import heapq
from typing import List


def merge_sorted_arrays(sorted_arrays: List[List[int]]):
    min_heap = []
    for array in sorted_arrays:
        for elem in array:
            heapq.heappush(min_heap, elem)
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result