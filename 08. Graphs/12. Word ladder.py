from collections import defaultdict, deque


def wordLadder(words, begin, end):
  # O(w * L^2) / O(w * L)
  L = len(begin)

  all_combo = defaultdict(list[str])
  for word in words:
    for i in range(L):
      pattern = word[:i] + '*' + word[i+1:]  # O(L)
      all_combo[pattern].append(word)

  queue = deque([(begin, 0)])
  visited = set([begin])  # / O(w)

  while queue:  # O(w)
    word, dist = queue.popleft()
    if word == end:
      return dist

    for i in range(L):  # O(L)
      pattern = word[:i] + '*' + word[i+1:]  # O(L)
      for nei in all_combo[pattern]:  # Total: O(w)
        if nei not in visited:
          visited.add(nei)
          queue.append((nei, dist + 1))

      all_combo[pattern] = []

  return -1


print(wordLadder(['hit', 'hot', 'dot', 'lot',
                  'dog', 'log', 'cog'], 'hit', 'cog'))
'''
Input: words = ['hit','hot','dot','lot','dog','log','cog']
begin = 'hit'
end = 'cog'
Output = 4
'''
# Usage: Find minimum steps to transform one word into another using BFS (Word Ladder)
# Useful for: shortest path in word graphs, interview problems, NLP edit distance approximations
