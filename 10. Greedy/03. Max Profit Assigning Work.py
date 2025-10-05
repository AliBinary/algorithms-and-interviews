def maxProfitAssignment(difficulty: list[int], profit: list[int], worker: list[int]):
  #  O(n log n + m log m) / O(m)
  jobs = []
  for i in range(len(profit)):  # O(m)
    jobs.append([difficulty[i], profit[i]])
  jobs.sort()  # O(m log m)
  worker.sort()  # O(n log n)
  maxTotalProfit = 0
  currJob = 0
  maxProfitForWorker = 0
  for worker in worker:
    while currJob < len(jobs) and jobs[currJob][0] <= worker:
      maxProfitForWorker = max(maxProfitForWorker, jobs[currJob][1])
      currJob += 1
    maxTotalProfit += maxProfitForWorker
  return maxTotalProfit


print(maxProfitAssignment([2, 4, 6, 8, 10],
      [10, 20, 30, 40, 50], [4, 5, 6, 7]))
'''
Input: difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
Output: 100
'''
# Usage: Assign workers to jobs maximizing profit (greedy + sort)
# Useful for: job assignment, scheduling, resource optimization
