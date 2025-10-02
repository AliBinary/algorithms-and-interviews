def BinarySubstrings(s: str) -> int:
    # O(n) / O(1)
    sol = 0
    len1 = 0
    len2 = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            len2 += 1
        else:
            sol += min(len1, len2)
            len1 = len2
            len2 = 1
    sol += min(len1, len2)
    return sol


print(BinarySubstrings('00110011'))
# Input: '00110011'
# Output: 6
# Input: '10101'
# Output: 4
# Usage: Count binary substrings with equal consecutive 0s and 1s
# Useful for: string analysis, pattern counting, binary sequences
