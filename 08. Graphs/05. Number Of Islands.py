def findMinDistances(n: int, m: int, grid: list[list[int]]):
  # O(n * m) / O(n * m)
  def dfs(i, j):
    visited[i][j] = True
    for x, y in [[i + 1, j], [i, j + 1],
                 [i - 1, j], [i, j - 1]]:
      if x >= 0 and x < n and y >= 0 and y < m and \
              grid[x][y] == 1 and not visited[x][y]:
        dfs(x, y)

  visited = [[False] * m for _ in range(n)]  # / O(n * m)
  numOfIslands = 0

  for i in range(n):
    for j in range(m):
      if grid[i][j] and not visited[i][j]:
        numOfIslands += 1
        dfs(i, j)  # Total: O(n * m)

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
# Usage: Count number of connected islands (1s) in a 2D grid using DFS
# Useful for: graph traversal on grids, flood fill, connected components
