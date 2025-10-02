def maxValue(nums, left, right):
  maxValue = nums[left]
  for i in range(left + 1, right + 1):
    maxValue = max(maxValue, nums[i])
  return maxValue


def computeSum(nums: list[int]) -> int:
  # O(n^3) / O(n)
  totalSum = 0
  for i in range(len(nums)):  # O(n)
    for j in range(i, len(nums)):  # O(n)
      totalSum += max(nums[i: j + 1])  # O(n) / O(n)
      # totalSum += maxValue(nums, i, j)  # O(n) / O(1)
  return totalSum


print(computeSum([2, 3, 4, 1]))
# Input: [2, 3, 4, 1]
# Output: 33
# Usage: Brute-force sum of maximums over all subarrays
# Useful for: subarray analysis, enumeration problems
