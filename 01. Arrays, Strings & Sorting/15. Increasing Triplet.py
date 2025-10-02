def increasingTriplet(nums: list[int]) -> bool:
    # O(n) / O(n)
    suffixMax = [0] * len(nums)
    suffixMax[-1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        suffixMax[i] = max(suffixMax[i + 1], nums[i])

    prefixMin = nums[0]
    for j in range(1, len(nums) - 1):
        if prefixMin < nums[j] and suffixMax[j + 1] > nums[j]:
            return True
        prefixMin = min(prefixMin, nums[j])
    return False


print(increasingTriplet([2, 1, 5, 0, 4, 6]))
# Input: [5, 4, 3, 2, 1]
# Output: false
# Input: [2, 1, 5, 0, 4, 6]
# Output: true
# Usage: Check if an increasing triplet subsequence exists in an array
# Useful for: subsequence problems, array analysis, greedy patterns
