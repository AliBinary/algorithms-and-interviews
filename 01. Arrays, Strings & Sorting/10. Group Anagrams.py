def groupAnagrams(strings: list[str]) -> list[list[str]]:
    # O(n log n)
    strings.sort(key=lambda word: ''.join(sorted(word)))
    currGroup = [strings[0]]
    groups = []
    for i in range(1, len(strings)):
        if sorted(strings[i]) == sorted(strings[i - 1]):
            currGroup.append(strings[i])
        else:
            groups.append(currGroup)
            currGroup = [strings[i]]
    groups.append(currGroup)
    return groups


print(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
# Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# Output: [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
# Usage: Group strings that are anagrams of each other
# Useful for: string manipulation, hashing, dictionary/trie problems
