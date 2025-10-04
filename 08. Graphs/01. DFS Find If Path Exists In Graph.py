from collections import defaultdict


def validPath(n: int, edges: list[list[int]], source: int, destination: int):
  # O(n + m) / O(n + m)
  def dfs(node):
    visited.add(node)  # Total: O(n)
    for adj_node in graph[node]:  # Total: O(m)
      if adj_node not in visited:
        dfs(adj_node)

  graph = defaultdict(list[int])  # / O(m)
  visited = set()  # / O(n)
  for edge in edges:  # O(m)
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

  dfs(source)
  return destination in visited


print(validPath(6, [[0, 1], [0, 2], [2, 3], [3, 5],
                    [5, 4], [4, 3]], 0, 5))
'''
Input: n = 6
edges = [[0, 1], [0, 2], [2, 3], [3, 5], [5, 4], [4, 3]]
source = 0,
destination = 5
Output: True
'''
# Usage: Check if there is a valid path between two nodes in an undirected graph
# Useful for: connectivity problems, graph traversal
