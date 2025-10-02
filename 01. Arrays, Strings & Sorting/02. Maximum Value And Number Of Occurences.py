def maxValNumOfOccurrences(nums: list[int]) -> list[int]:
  # O(n) / O(1)
  maxVal = nums[0]
  counter = 0
  for num in nums:
    if num > maxVal:
      maxVal = num
      counter = 1
    elif num == maxVal:
      counter += 1
  return [maxVal, counter]


print(maxValNumOfOccurrences([2, 7, 11, 8, 11, 8, 3, 11]))
# Input: [2, 7, 11, 8, 11, 8, 3, 11]
# Output: [11, 3]
# Usage: Find the maximum value in an array and count its occurrences
# Useful for: array analysis, frequency counting, selection problems
