def minimumAbsDifference(nums: list[int]) -> list[list[int]]:
  # O(n log n) / O(n^2)
  nums.sort()
  minDiff = nums[1] - nums[0]
  minDiffPairs = []
  for i in range(1, len(nums)):
    curDiff = nums[i] - nums[i - 1]
    if curDiff < minDiff:
      minDiff = curDiff
      minDiffPairs = [[nums[i - 1], nums[i]]]
    elif curDiff == minDiff:
      minDiffPairs.append([nums[i - 1], nums[i]])
  return minDiffPairs


print(minimumAbsDifference([4, 2, 1, 3]))
# Input: [4, 2, 1, 3]
# Output: [[1, 2], [2, 3], [3, 4]]
# Input: [3, 8, -10, 23, 19, -4, -14, 27]
# Output: [[-14, -10], [19, 23], [23, 27]]
# Usage: Find all pairs with minimum absolute difference in a list
# Useful for: array sorting problems, consecutive pair analysis
