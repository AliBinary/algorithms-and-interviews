def maxSumSubArray(nums: list[int]) -> int:
    # O(n^2) / O(1)
    greatestSum = nums[0]
    for i in range(len(nums)):  # O(n)
        currentSum = 0
        for j in range(i, len(nums)):  # O(n)
            currentSum += nums[j]  # O(1)
            greatestSum = max(greatestSum, currentSum)
    return greatestSum


print(maxSumSubArray([-2, -5, 6, -2, -3, 1, 5, -6]))
# Input: [-2, -5, 6, -2, -3, 1, 5, -6]
# Output: 7
# Explanation: sum([6, -2, -3, 1, 5]) = 7
# Usage: Brute-force maximum subarray sum
# Useful for: array subproblems, Kadane’s algorithm comparison
