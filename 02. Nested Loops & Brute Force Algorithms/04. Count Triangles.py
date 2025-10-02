def isTriangle(num1, num2, num3):  # O(1)
  return num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1


def countTriangles(nums: list[int]) -> int:
  # O(n^3) / O(1)
  solution = 0
  for i in range(len(nums)):  # O(n)
    for j in range(i + 1, len(nums)):  # O(n)
      for k in range(j+1, len(nums)):  # O(n)
        if isTriangle(nums[i], nums[j], nums[k]):
          solution += 1
  return solution


print(countTriangles([3, 5, 10, 7]))
# Input: [3, 5, 10, 7]
# Output: 2
# Explanation: (3, 5, 7), (5, 10, 7)
# Usage: Count number of triplets forming valid triangles
# Useful for: geometry problems, combinatorial enumeration
