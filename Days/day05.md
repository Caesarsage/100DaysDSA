## Array operations

- [Inserting](day05.md)
- [Deleting](day06.md)
- [Searching](day07.md)

### Inserting

Inserting a new element into an Array can take many forms :

- inserting element at the end of the Array
- Inserting at the beginning of the Array
- Inserting a new element at any given index inside the Array


### inserting element at the end of the Array

At any point in time, we know the index of the last element of the Array, as we kep track of if in our `length` variable.
All we need to do for inserting an element at the end is to assign the new element to one index past the current element

### Inserting at the Start of an Array

To insert an element at the start of an Array, we'll need to shift all other elements in the Array to the right by one index to create space for the new element. This is a very costly operation, since each of the existing elements has to be shifted one step to the right. The need to shift everything implies that this is not a constant time operation. In fact, the time taken for insertion at the beginning of an Array will be proportional to the length of the Array. 

In terms of time complexity analysis, this is a linear time complexity: O(N)O(N), where NN is the length of the Array.

### Inserting at the End of an Array

Similarly, for inserting at any given index, we first need to shift all the elements from that index onwards one position to the right.

Once the space is created for the new element, we proceed with the insertion. If you think about it, insertion at the beginning is basically a special case of inserting an element at a given index—in that case, the given index was 0.

## Questions

- [Duplicate Zeros](../Solutions/duplicate_zeros.py)
- [Merge sorted arr](../Solutions/merge_sorted_arr.py)

## Solution thought flow

Q1.

> Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

- Iterate through the length of the arr
- if each num in the array is zero, insert a new zero at that index+1 
- for each insertion delete and last element
- increase the index twices
- else, increase the index onces
  
Q2.

> You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

> Merge nums1 and nums2 into a single array sorted in non-decreasing order.

> The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


- Using two pointers
- since first array is large enough for the other accommodation
- Have a pointer to the last zero in arr1. (last = m+n-1)
- while arr1 integer(m) and arr2 integer(n) are greater than zero
  - check if last non-zero integer of array1 is greater than last index of array2, make last arr1 index equal to last arr1 non-zero number and decrease m.
  - else, make the last arr1 num equal to last arr2 number and decrease n
- finally decrease last created at the beginning for both case
- fill arr1 with left over element just incase by
- while n is greater than 0
- set arr1 last element equal to arr2 last non-zero element
- swap n and last with n-1 and last -1

###### I am  welcoming any more optimized solution you have, Make a PR
## we move

see you on <a href="./day06.md">Day 06</a>