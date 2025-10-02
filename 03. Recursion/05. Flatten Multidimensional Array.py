def flatten(item):
  # O(number of int items * maxDepth)
  # / O(number of int items * maxDepth)
  if type(item) is int:  # base case
    return [item]
  flattened_array = []
  for inner_item in item:
    flattened_array += flatten(inner_item)
  return flattened_array


print(flatten([[[1, 2], 3], [[5, [6]], 7], 8]))
# Input: [0, [1, [2]], [[[3]]]]
# Output: [0, 1, 2, 3]
# Usage: Flatten a nested list of integers into a single flat list
# Useful for: recursion, tree-like structures, nested data processing
