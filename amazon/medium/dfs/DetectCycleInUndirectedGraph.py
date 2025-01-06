from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        node = None
        for edge in edges:
            if not node:
                node = edge[0]
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        def has_cycle(curr_node, parent_node):
            visited.add(curr_node)

            for nei in graph[curr_node]:
                if nei not in visited:
                    if has_cycle(nei, curr_node):
                        return True
                elif nei != parent_node: # if it's not the same, we know it's wrong
                    return True
            return False
    
        for node in graph:
            if node not in visited:
                if has_cycle(node, None):
                    return True
        return False
