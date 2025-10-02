from collections import deque


def findMinDistances(n, m, grid):
  # O(n * m) / O(n * m)
  def discoverNewIsland():
    islands[i][j] = numOfIslands
    queue.append([i, j])

    while queue:  # Total: O(n * m)
      node = queue.popleft()
      for x, y in [[node[0] + 1, node[1]],
                   [node[0], node[1] + 1],
                   [node[0] - 1, node[1]],
                   [node[0], node[1] - 1]]:
        if x < 0 or x >= n or y < 0 or y >= m or \
                grid[x][y] == 0 or islands[x][y] != -1:
          continue
        islands[x][y] = numOfIslands
        queue.append([x, y])

  queue = deque()
  islands = [[-1] * m for _ in range(n)]  # / O(n * m)
  numOfIslands = 0

  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1 and islands[i][j] == -1:
        numOfIslands += 1
        discoverNewIsland()

  return numOfIslands


print(findMinDistances(4, 5, [[1, 1, 0, 0, 0],
                              [1, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 1]]))
'''
Input: n = 4, m = 5
grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]]
Output: 3
'''
# Usage: Count number of connected islands (1s) in a 2D grid using BFS
# Useful for: graph traversal on grids, flood fill, connected components
