# Definition for singly-linked list.
class ListNode:
  def __init__(self, x, next=None, random=None):
    self.val = x
    self.next = next
    self.random = random


def copyRandomList(head: ListNode) -> ListNode:
  # O(n) / O(1)
  if not head:
    return None

  # Step 1: Insert copy node right after each original node
  node = head
  while node:
    nextNode = node.next
    copyNode = ListNode(node.val)
    node.next = copyNode
    copyNode.next = nextNode
    node = nextNode

  # Step 2: Assign random pointers for the copied nodes
  node = head
  while node:
    copyNode = node.next
    if node.random:
      copyNode.random = node.random.next
    node = copyNode.next

  # Step 3: Separate the original list and the copied list
  newHead = head.next
  node = head
  while node:
    copyNode = node.next
    nextNode = copyNode.next
    if nextNode:
      copyNode.next = nextNode.next
    node.next = nextNode
    node = nextNode

  return newHead


# Usage: Deep copy linked list with next & random pointers
# Useful for: linked list cloning, O(1) extra space trick
# Example usage:
# Create nodes
a = ListNode(7)
b = ListNode(13)
c = ListNode(11)
d = ListNode(10)
e = ListNode(1)
# Link with next pointers
a.next = b
b.next = c
c.next = d
d.next = e
# Link with random pointers
a.random = None
b.random = a
c.random = e
d.random = c
e.random = a
# Copy the list
copied_head = copyRandomList(a)
# Print copied list: show value and random value if exists
node = copied_head
while node:
  rand_val = node.random.val if node.random else None
  print(f"Node({node.val}), Random -> {rand_val}")
  node = node.next
