def majorityElement(nums: list[int]) -> int:
  # O(n log n) / O(1)
  counter = 1
  maxCounter = 1
  solution = nums[0]
  nums.sort()
  for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
      counter += 1
    else:
      counter = 1
    if counter > maxCounter:
      maxCounter = counter
      solution = nums[i - 1]
  return solution


print(majorityElement([2, 2, 1, 1, 1, 3, 3, 3, 3]))
# Input: [3, 2, 3]
# Output: 3
# Input: [2, 2, 1, 1, 1, 2, 2]
# Output: 2
# Usage: Find the element that appears more than half of the array
# Useful for: array analysis, frequency counting, voting problems
