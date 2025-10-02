from collections import defaultdict, deque


def findMinDistances(n, edges, source):
  # O(n + m) / O(n + m)
  graph = defaultdict(list[int])  # / O(m)
  for edge in edges:  # O(m)
    graph[edge[0]].append(edge[1])
    # graph[edge[1]].append(edge[0])

  queue = deque([source])
  minDist = [-1] * n  # / O(n)
  minDist[source] = 0

  while queue:  # Total: O(n + m)
    node = queue.popleft()  # Total: O(n)
    for adj_node in graph[node]:  # Total: O(m)
      if minDist[adj_node] == -1:
        minDist[adj_node] = minDist[node] + 1
        queue.append(adj_node)

  return minDist


print(findMinDistances(8, [[0, 1], [0, 2], [0, 3],
                           [2, 1], [3, 4], [4, 2],
                           [4, 6], [4, 5], [5, 6],
                           [6, 7]], 0))
'''
Input: n = 8
edges = [[0, 1], [0, 2], [0, 3], [2, 1], [3, 4],
         [4, 2], [4, 6], [4, 5], [5, 6], [6, 7]]
source = 0,
Output: [0, 1, 1, 1, 2, 3, 3, 4]
'''
