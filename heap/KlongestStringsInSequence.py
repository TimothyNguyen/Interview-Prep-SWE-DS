import heapq
import itertools


def k_longest_string_in_seq(k, stream):
    # Entries are compared by their lengths
    min_heap = [(len(s), s) for s in itertools.isslice(stream, k)]
    heapq.heappify(min_heap)
    for next_string in stream:
        # push next_string and pop the shortest string in min_heap
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]