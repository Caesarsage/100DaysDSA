## Array operations

- [Inserting](day05.md)
- [Deleting](day06.md)
- [Searching](day07.md)

### Deleting

Deletion in an Array works in a very similar manner to insertion, and has the same three different cases:

- Deleting the last element of the Array.
- Deleting the first element of the Array.
- Deletion at any given index.

#### Deleting the last element of the Array

Deletion at the end of an Array is similar to people standing in a line, also known as a queue. The person who most recently joined the queue (at the end) can leave at any time without disturbing the rest of the queue. Deleting from the end of an Array is the least time consuming of the three cases. Recall that insertion at the end of an Array was also the least time-consuming case for insertion.

```

Deletion from the end is as simple as reducing the length
// of the array by 1.
length--;

```

#### Deleting the first element if the Array

Next comes the costliest of all deletion operations for an Array—deleting the first element. If we want to delete the first element of the Array, that will create a vacant spot at the 0th index. To fill that spot, we will shift the element at index 1 one step to the left. Going by the ripple effect, every element all the way to the last one will be shifted one place to the left. This shift of elements takes O(N)O(N) time, where NN is the number of elements in the Array.
#### Deletion at any given index

For deletion at any given index, the empty space created by the deleted item will need to be filled. Each of the elements to the right of the index we're deleting at will get shifted to the left by one. Deleting the first element of an Array is a special case of deletion at a given index, where the index is 0. This shift of elements takes O(K)O(K) time where KK is the number of elements to the right of the given index. Since potentially K = NK=N, we say that the time complexity of this operation is also O(N)O(N).
## Questions

- [Remove Element](../Solutions/remove_element.py)
- [Remove Duplicates from sorted array](../Solutions/remove_duplicate_sorted_arr.py)

## Solution thought flow

Q1.

> Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

- Set a variable left_pointer to 0, this variable is going to keep track of where to put the next non given val.
- iterate with a for loop to scan through the array of numbers 
- check if the current num in the array is not  equal to the given value and make the left_pointer equal to that num if true, then increment the left pointer
- otherwise the loops keep on scanning
- at end of the loop, return the left pointer.

Q2.

> Return k after placing the final result in the first k slots of nums.
  Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

- Set a variable left_pointer to 1, this variable is going to keep track of where to put the next unique value.(we are starting with 1 because the first number in the array will always be unique)
- iterate with a for loop to scan through the array of numbers 
- check if the current num in the array is not equal to the previous value and make the left_pointer equal to that num if true, then increment the left pointer
- otherwise the loops keep on scanning
- at end of the loop, return the left pointer.

###### I am  welcoming any more optimized solution you have, Make a PR

# we move

see you on <a href="./day07.md">Day 07</a>
