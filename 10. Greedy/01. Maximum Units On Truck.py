def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:
  # O(n log n) / O(1)
  noOfUnits = 0
  boxTypes.sort(key=lambda boxType: -boxType[1])  # O(n log n)
  for boxType in boxTypes:  # O(n)
    boxesToTake = min(boxType[0], truckSize)
    noOfUnits += boxesToTake * boxType[1]
    truckSize -= boxesToTake
    if truckSize == 0:
      break
  return noOfUnits


print(maximumUnits([[1, 3], [2, 2], [3, 1]], 4))
'''
Input: boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
Output: 8
Input: boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
Output: 91
'''
# Usage: Maximize units loaded into truck by greedy sort
# Useful for: greedy knapsack-like problems
