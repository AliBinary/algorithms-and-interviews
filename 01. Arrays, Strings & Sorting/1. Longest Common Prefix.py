def areEqual(strs, index):
    for i in range(1, len(strs)):  # O(n)
        if strs[i][index] != strs[0][index]:
            return False
    return True


def longestCommonPrefix(strs: list[str]) -> str:
    # O(n * L) / O(L)
    minLength = len(strs[0])
    for i in range(1, len(strs)):  # O(n)
        minLength = min(minLength, len(strs[i]))
    # minLength = min([len(word) for word in strs]) # O(n * L)
    longestCommonPrefix = ''
    for i in range(minLength):  # O(L)
        if areEqual(strs, i):  # O(n)
            longestCommonPrefix += strs[0][i]  # O(1)
        else:
            break
    return longestCommonPrefix  # O(L)


print(longestCommonPrefix(['flower',
                           'flow',
                           'flood',
                           'flair']))
'''
Input: ['flower',
        'flow',
        'flood',
        'flair']
Output: 'fl'
'''
# Usage: Find the longest common prefix among multiple strings
# Useful for: string processing, dictionary/trie problems, prefix analysis
