def findMaxConsecutiveOnes(nums: list[int]) -> int:
  # O(n) / O(1)
  counter = 0
  solution = 0
  for num in nums:
    if num == 1:
      counter += 1
    else:
      counter = 0
    solution = max(solution, counter)
  return counter


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
# Input: [1, 1, 0, 1, 1, 1]
# Output: 3
# Input: [1, 0, 1, 1, 0, 1]
# Output: 2
# Usage: Find the maximum number of consecutive ones in a binary array
# Useful for: array analysis, binary sequences, sliding window problems
