def rotate(nums: list[int]) -> None:
  # O(n) / O(1)
  aux_val = nums[-1]
  for i in range(len(nums)-1, 0, -1):
    nums[i] = nums[i - 1]
  nums[0] = aux_val
  return nums


print(rotate([1, 2, 3, 4, 5]))
# Input: [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
# Input: [4, -2, 13, 1]
# Output: [1, 4, -2, 13]
# Usage: Rotate elements of an array by one position to the right
# Useful for: array manipulation, cyclic shifts, in-place operations
