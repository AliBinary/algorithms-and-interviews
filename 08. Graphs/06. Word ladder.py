from collections import deque


def getStarWord(word, i):
  return word[:i] + "*" + word[i + 1:]


def ladderLength(words: list[str], beginWord: str, endWord: str) -> int:
  # O(w * L^2) / O(w * L)
  graph = {}  # / O(w * L)
  for word in words:  # O(w)
    for i in range(len(word)):  # O(L)
      starWord = getStarWord(word, i)  # O(L)
      graph[starWord] = graph.get(starWord, []) + [word]

  queue = deque()  # / O(w)
  minDist = {}
  queue.append(beginWord)
  minDist[beginWord] = 1

  while queue:  # O(w)
    word = queue.popleft()
    if endWord == word:
      break
    for i in range(len(word)):  # O(L)
      starWord = getStarWord(word, i)  # O(L)
      for nextWord in graph.get(starWord, []):  # Total: O(w * L)
        if nextWord not in minDist:
          minDist[nextWord] = minDist[word] + 1
          queue.append(nextWord)
  return minDist.get(endWord, 0)


print(ladderLength(['hit', 'hot', 'dot', 'lot',
                    'dog', 'log', 'cog'], 'hit', 'cog'))
'''
Input: words = ['hit','hot','dot','lot','dog','log','cog']
begin = 'hit'
end = 'cog'
Output = 5
'''
