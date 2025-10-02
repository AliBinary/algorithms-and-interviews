def isDuplicate(nums, index):
    if index > 0 and nums[index] == nums[index - 1]:
        return False
    if index == len(nums) - 1 or nums[index] != nums[index + 1]:
        return False
    return True


def findDuplicates(nums: list[int]) -> list[int]:
    # O(n log n) / O(n)
    nums.sort()
    duplicates = []
    for i in range(len(nums)):
        if isDuplicate(nums, i):
            duplicates.append(nums[i])
    return duplicates


print(findDuplicates([1, 5, 1, 2, 3, 5, 4]))
# Input: [2, 3, 1, 1, 4, 3, 2, 1]
# Output: [2, 1, 3]
# Usage: Find all elements that appear more than once in an array
# Useful for: array analysis, counting duplicates, sorting-based problems
