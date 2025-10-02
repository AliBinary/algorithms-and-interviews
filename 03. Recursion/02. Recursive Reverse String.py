def reverse(s: str) -> str:
  # O(n^2) / O(n^2)
  if not s:
    return ""
  return s[-1] + reverse(s[:-1])  # O(len) / O(len)


print(reverse('abcde'))
# Input: 'abcde'
# Output: 'edcba'
# Usage: Reverse a string using recursion
# Useful for: recursion practice, string manipulation
