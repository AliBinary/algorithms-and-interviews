def secondLargest(nums: list[int]) -> int:
  # O(n) / O(1)
  largest = secondLargest = None
  for num in nums:
    if not largest or num > largest:
      secondLargest = largest
      largest = num
    elif num != largest and (not secondLargest or num > secondLargest):
      secondLargest = num
  return secondLargest


print(secondLargest([1000, 100, 100]))
# Input: [2, 7, 11, 8, 11, 8, 3, 11]
# Output: 8
# Input: [1000, 100, 100]
# Output: 100
# Usage: Find the second largest element in an array
# Useful for: array analysis, selection problems, in-place operations
