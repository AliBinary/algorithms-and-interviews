def maxSumOf3SubArrays(nums: list[int]):
  # O(n) / O(n)
  n = len(nums)
  leftMaxSum = [0] * n  # / O(n)

  leftMaxSum[1] = nums[0]
  maxSum = nums[0]

  for i in range(2, n):  # O(n)
    maxSum = nums[i - 1] + max(maxSum, 0)
    leftMaxSum[i] = max(leftMaxSum[i - 1], maxSum)

  rightMaxSum = [0] * n  # / O(n)

  rightMaxSum[-1] = nums[-1]
  maxSum = nums[-1]

  for i in range(n - 2, -1, -1):  # O(n)
    maxSum = nums[i] + max(maxSum, 0)
    rightMaxSum[i] = max(rightMaxSum[i + 1], maxSum)

  partialSums = [0]  # / O(n)
  for i in range(n):  # O(n)
    partialSums.append(partialSums[i] + nums[i])

  maxSum = float('-inf')
  maxDiff = float('-inf')
  for right2 in range(1, len(nums) - 1):  # O(n)
    maxDiff = max(maxDiff, leftMaxSum[right2] - partialSums[right2])
    maxSum = max(maxSum, partialSums[right2 + 1] +
                 rightMaxSum[right2 + 1] + maxDiff)

  return maxSum


print(maxSumOf3SubArrays([2, 3, -8, 7, -2, 9, -9, 7, -2, 4]))
# Input: [2, 3, -8, 7, -2, 9, -9, 7, -2, 4]
# Output: 28
# Usage: Max sum of 3 non-overlapping subarrays using prefix + DP
# Useful for: array DP, max subarray problems, interview-style challenges
