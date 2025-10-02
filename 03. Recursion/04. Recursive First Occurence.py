def firstOccurence(nums: list[int], value: int) -> int:
  # O(n^2) / O(n^2)
  if not nums:
    return -1
  index = firstOccurence(nums[:-1], value)  # O(len)
  if index != -1:
    return index
  if value == nums[-1]:
    return len(nums) - 1
  return -1


print(firstOccurence([1, 3, 5, 7, 9], 11))
# Input: [2, 4, 8, 6, 8, 10], 8
# Output: 2
# Input: [1, 3, 5, 7, 9], 11
# Output: -1
# Usage: Find the first occurrence of a value in an array using recursion
# Useful for: recursion practice, search problems
