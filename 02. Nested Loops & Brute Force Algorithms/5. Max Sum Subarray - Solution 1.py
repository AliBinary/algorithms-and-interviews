def maxSumSubArray(nums: list[int]) -> int:
    # O(n^3) / O(n)
    greatestSum = nums[0]
    for i in range(len(nums)):  # O(n)
        for j in range(i, len(nums)):  # O(n)
            currentSum = sum(nums[i: j + 1])  # O(n) / O(n)
            greatestSum = max(greatestSum, currentSum)  # O(1)
    return greatestSum


print(maxSumSubArray([-2, -5, 6, -2, -3, 1, 5, -6]))
# Input: [-2, -5, 6, -2, -3, 1, 5, -6]
# Output: 7
# Explanation: sum([6, -2, -3, 1, 5]) = 7
# Usage: Brute-force maximum subarray sum
# Useful for: array subproblems, Kadane’s algorithm comparison
