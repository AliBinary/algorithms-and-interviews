from collections import defaultdict, deque


def getAnswer(dist1, dist2):
  if dist1 == -1:
    return dist2
  if dist2 == -1:
    return dist1
  return min(dist1, dist2)


def shortestAlternatingPaths(n: int, redEdges: list[list[int]], blueEdges: list[list[int]], source: int):
  # O(n + m) / O(n + m)
  graph = defaultdict(list)  # / O(n + m)
  for edge in redEdges:
    graph[edge[0]].append([edge[1], 0])
    # graph[edge[1]].append([edge[0], 0])
  for edge in blueEdges:
    graph[edge[0]].append([edge[1], 1])
    # graph[edge[1]].append([edge[0], 1])

  queue = deque([[source, 0], [source, 1]])
  minDist = [[-1, -1] for _ in range(n)]  # O(n)
  minDist[source][0] = minDist[source][1] = 0

  while queue:  # Total: O(n + m)
    [node, last_color] = queue.popleft()
    for [adj_node, edge_color] in graph[node]:  # Total: O(m)
      if edge_color != last_color and minDist[adj_node][edge_color] == -1:
        minDist[adj_node][edge_color] = minDist[node][last_color] + 1
        queue.append([adj_node, edge_color])

  answer = []
  for node in range(n):  # O(n)
    answer.append(getAnswer(minDist[node][0], minDist[node][1]))

  return answer


print(shortestAlternatingPaths(7, [[0, 1], [1, 3], [2, 3], [3, 5], [4, 5]],
                               [[0, 2], [2, 6], [2, 4], [3, 4]], 0))
'''
Input: n = 7
redEdges = [[0, 1], [1, 3], [2, 3], [3, 5], [4, 5]]
blueEdges = [[0, 2], [2, 6], [2, 4], [3, 4]]
source = 0,
Output: [0, 1, 1, 2, 3, 4, -1]
'''
# Usage: Find shortest paths in a graph with alternating edge colors
# Useful for: BFS traversal, graph problems with edge constraints, shortest path analysis
