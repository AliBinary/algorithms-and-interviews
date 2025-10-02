from collections import defaultdict
import heapq  # MAX HEAP!!!


def findMinDistances(n, edges, source):
    # O((m + n) log m) / O(m)
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append([edge[1], edge[2]])
        # graph[edge[1]].append([edge[0], edge[2]])

    min_heap = []
    heapq.heappush(min_heap, [0, source])
    minDist = [-1] * n
    minDist[source] = 0
    while min_heap:
        [distance, node] = heapq.heappop(min_heap)
        distance *= -1
        if distance != minDist[node]:
            continue
        for [adj_node, weight] in graph[node]:
            currDist = minDist[node] + weight
            if minDist[adj_node] == -1 or minDist[adj_node] > currDist:
                minDist[adj_node] = currDist
                heapq.heappush(min_heap, [-currDist, adj_node])

    return minDist


print(findMinDistances(7, [[0, 1, 6], [0, 2, 2], [2, 1, 3],
                           [1, 4, 2], [2, 3, 1], [3, 1, 1],
                           [3, 4, 2], [4, 5, 1], [4, 6, 3]], 0))
'''
Input: n = 7
edges = [[0, 1, 6], [0, 2, 2], [2, 1, 3], [1, 4, 2], [2, 3, 1],
                    [3, 1, 1], [3, 4, 2], [4, 5, 1], [4, 6, 3]]
source = 0,
Output: [0, 4, 2, 3, 5, 6, 8]
'''
