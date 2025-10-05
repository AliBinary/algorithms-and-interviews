def nonOverlappingIntervals(intervals: list[list[int]]) -> int:
  # O(n log n) / O(1)
  intervals.sort(key=lambda interval: interval[1])  # O(n log n)
  result, lastTaken = 1, 0
  for i in range(1, len(intervals)):  # O(n)
    if intervals[i][0] >= intervals[lastTaken][1]:
      result += 1
      lastTaken = i
  return result


print(nonOverlappingIntervals([[1, 3], [2, 4],
                               [3, 5], [3, 8],
                               [7, 9], [9, 12],
                               [6, 12]]))
'''
Input: [[1, 3], [2, 4], [3, 5], [3, 8],
              [7, 9], [9, 12], [6, 12]]
Output: 4
'''
# Usage: Find max non-overlapping intervals (greedy by end time)
# Useful for: interval scheduling, activity selection
