def computeSum(nums: list[int]) -> int:
    # O(n^2) / O(1)
    totalSum = 0
    for i in range(len(nums)):  # O(n)
        curMax = nums[i]
        for j in range(i, len(nums)):  # O(n)
            curMax = max(curMax, nums[j])
            totalSum += curMax
    return totalSum


print(computeSum([2, 3, 4, 1]))
# Input: [2, 3, 4, 1]
# Output: 33
# Usage: Brute-force sum of maximums over all subarrays
# Useful for: subarray analysis, enumeration problems
