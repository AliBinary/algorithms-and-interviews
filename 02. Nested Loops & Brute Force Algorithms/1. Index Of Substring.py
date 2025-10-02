def isSubstring(haystack, needle, start):  # O(m)
    for i in range(len(needle)):
        if needle[i] != haystack[start + i]:
            return False
    return True


def indexOf(haystack: str, needle: str) -> int:
    # O(n * m) / O(1)
    n = len(haystack)
    m = len(needle)
    for i in range(n - m + 1):  # O(n - m)
        if isSubstring(haystack, needle, i):  # O(m)
            return i
    return -1


print(indexOf('hello', 'll'))
# Input: "hello", "ll"
# Output: 2
# Input: "aaaaa", "bba"
# Output: -1
# Usage: Find the first occurrence of a substring in a string
# Useful for: string search, naive pattern matching problems
