def sum(nums: list[int]) -> int:
    # O(n^2) / O(n^2)
    if not nums:
        return 0
    return nums[0] + sum(nums[1:])  # O(len) / O(len)


print(sum([1, 2, 3, 4, 5]))
# Input: [1, 2, 3, 4, 5]
# Output: 15
