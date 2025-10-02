def numOfDistinctValues(nums: list[int]) -> int:
  # O(n log n) / O(1)
  sol = 1
  nums.sort()
  for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
      sol += 1
  return sol


print(numOfDistinctValues([1, 5, -3, 1, -4, 2, -4, 7, 7]))
# Input: [1, 5, -3, 1, -4, 2, -4, 7, 7]
# Output: 6
# Usage: Count the number of distinct elements in an array
# Useful for: array analysis, duplicates handling, sorting-based problems
