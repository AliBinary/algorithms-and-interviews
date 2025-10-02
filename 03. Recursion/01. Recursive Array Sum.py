def sum(nums: list[int]) -> int:
  # O(n^2) / O(n^2)
  if not nums:
    return 0
  return nums[0] + sum(nums[1:])  # O(len) / O(len)


print(sum([1, 2, 3, 4, 5]))
# Input: [1, 2, 3, 4, 5]
# Output: 15
# Usage: Compute the sum of an array using recursion
# Useful for: recursion practice, divide-and-conquer illustration
