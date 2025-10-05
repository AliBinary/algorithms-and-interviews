def findContentChildren(g: list[list], s: list[int]) -> int:
  # O(n log n) + O(m log m)
  g.sort()  # O(n log n)
  s.sort()  # O(m log m)
  i, j = 0, 0
  solution = 0
  while i < len(g) and j < len(s):  # O(n + m)
    if g[i] > s[j]:
      j += 1
    else:
      solution += 1
      i += 1
      j += 1
  return solution


print(findContentChildren([1, 2, 3], [1, 1]))
'''
Input: g = [1, 2, 3]
s = [1, 1]
Output: 1
Input: g = [2, 3, 5, 7]
s = [1, 2, 5, 6, 6]
Output: 3
'''
# Usage: Assign cookies to maximize content children (greedy)
# Useful for: greedy matching, resource allocation
