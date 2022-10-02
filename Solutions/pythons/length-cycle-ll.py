# Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.

# Solution: We can use the above solution to find the cycle in the LinkedList. Once the fast and slow pointers meet, we can save the slow pointer and iterate the whole cycle with another pointer until we see the slow pointer again to find the length of the cycle.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_length(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
      curr = slow
      circle_count = 0
      while True:
        curr = curr.next
        circle_count += 1
        if slow == curr:
          break
      return circle_count
