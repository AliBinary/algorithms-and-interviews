def isSingleNumber(nums, index):
  if index > 0 and nums[index - 1] != nums[index]:
    return False
  if index < len(nums) - 1 and nums[index] != nums[index + 1]:
    return False
  return True


def singleNumber(nums: list[int]) -> int:
  # O(n log n)
  if len(nums) == 1:
    return nums[0]
  nums.sort()
  for i in range(0, len(nums)):
    if isSingleNumber(nums, i):
      return nums[i]


print(singleNumber([4, 1, 2, 1, 2]))
# Input: [2, 2, 1]
# Output: 1
# Input: [4, 1, 2, 1, 2]
# Output: 4
# Usage: Find the element that appears exactly once in an array
# Useful for: array analysis, duplicates handling, sorting-based problems
