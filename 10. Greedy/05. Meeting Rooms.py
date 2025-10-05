def meetingRooms(intervals: list[list[int]]) -> int:
  # O(n log n) / O(n)
  events = []  # / O(n)
  for start, end in intervals:  # O(n)
    events.append([start, 1])
    events.append([end, -1])

  events.sort()  # O(n log n)

  answer, noOfMeetings = 0, 0
  for time, type in events:  # O(n)
    noOfMeetings += type
    answer = max(answer, noOfMeetings)

  return answer


print(meetingRooms([[1, 5], [2, 7], [0, 9], [5, 8], [7, 11]]))
# Input: [[1, 5], [2, 7], [0, 9], [5, 8], [7, 11]]
# Output: 3
# Usage: Find minimum meeting rooms needed (max overlaps)
# Useful for: interval overlap, resource allocation
