from collections import defaultdict
import heapq  # MAX HEAP!!!


def findMinDistances(n: int, edges: list[list[int]], source: int):
  # O((m + n) log m) / O(m + n)
  graph = defaultdict(list)  # / O(m)
  for edge in edges:  # O(m)
    graph[edge[0]].append([edge[1], edge[2]])
    # graph[edge[1]].append([edge[0], edge[2]])

  min_heap = []
  heapq.heappush(min_heap, [0, source])
  minDist = [-1] * n  # / O(n)
  minDist[source] = 0

  while min_heap:  # Total: O((m + n) log m)
    [distance, node] = heapq.heappop(min_heap)
    distance *= -1
    if distance != minDist[node]:
      continue
    for [adj_node, weight] in graph[node]:  # Total: O(m)
      currDist = minDist[node] + weight
      if minDist[adj_node] == -1 or minDist[adj_node] > currDist:
        minDist[adj_node] = currDist
        heapq.heappush(min_heap, [-currDist, adj_node])

  return minDist


print(findMinDistances(7, [[0, 1, 6], [0, 2, 2], [2, 1, 3],
                           [1, 4, 2], [2, 3, 1], [3, 1, 1],
                           [3, 4, 2], [4, 5, 1], [4, 6, 3]], 0))
'''
Input: n = 7
edges = [[0, 1, 6], [0, 2, 2], [2, 1, 3], [1, 4, 2], [2, 3, 1],
                    [3, 1, 1], [3, 4, 2], [4, 5, 1], [4, 6, 3]]
source = 0,
Output: [0, 4, 2, 3, 5, 6, 8]
'''
# Usage: Find shortest paths from a source node in a weighted graph (Dijkstra)
# Useful for: graph traversal, shortest path problems, network analysis
