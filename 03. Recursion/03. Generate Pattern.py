def pattern(n: int) -> list[int]:
  # O(n^2) / O(n^2)
  if n == 0:
    return []  # O(1)
  halfPattern = pattern(n - 1)  # O(len) / O(len)
  return halfPattern + [n] + halfPattern


print(pattern(4))
# Input: 3
# Output: [1, 2, 1, 3, 1, 2, 1]
# Input: 4
# Output: [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
# Usage: Generate recursive symmetric patterns
# Useful for: recursion practice, divide-and-conquer patterns
