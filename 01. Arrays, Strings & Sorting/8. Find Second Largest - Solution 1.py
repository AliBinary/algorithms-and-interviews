def secondLargest(nums: list[int]) -> int:
    # O(n log n) / O(1)
    nums.sort(reverse=True)
    for num in nums:
        if num != nums[0]:
            return num


print(secondLargest([2, 7, 11, 8, 11, 8, 3, 11]))
# Input: [2, 7, 11, 8, 11, 8, 3, 11]
# Output: 8
# Usage: Find the second largest element by sorting the array
# Useful for: array analysis, selection problems
