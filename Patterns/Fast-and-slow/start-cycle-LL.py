# Start of LinkedList Cycle (medium)
# Problem Statement
# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  # TODO: Write your code here
  fast, slow = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      cycle_length = calculate_cycle_length(slow)
      break
  return cal_start_head(head, cycle_length)


def calculate_cycle_length(slow):
  curr = slow
  cycle_length = 0
  while True:
    curr = curr.next
    cycle_length += 1
    if slow == curr:
      break
  return cycle_length


def cal_start_head(head, cycle_length):
  pointer1 = head
  pointer2 = head

  while cycle_length > 0:
    pointer2 = pointer2.next
    cycle_length -= 1
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next

  return pointer1


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
