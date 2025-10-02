def isSolution(s, length):  # O(n) / O(1)
    if len(s) % length:
        return False
    count = int(len(s) / length)
    for index in range(length):  # O(length)
        for group in range(1, count):  # O(count)
            if s[index] != s[index + group * length]:
                return False
    return True


def repeatedSubstringPattern(s: str) -> bool:
    # O(n^2) / O(1)
    for length in range(1, len(s)):  # O(n)
        if isSolution(s, length):  # O(n)
            return True
    return False


print(repeatedSubstringPattern('abcabcabcabc'))
# Input: 'abab'
# Output: true
# Input: 'aba'
# Output: false
# Input: 'abcabcabcabc'
# Output: true
# Usage: Check if a string is composed of repeated substring(s)
# Useful for: string pattern matching, periodicity detection
