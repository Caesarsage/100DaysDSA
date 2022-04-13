## Array operations

- Inserting
- Deleting
- Searching

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

- [Maximum Consecutive Ones](../ProblemsAndSolutions/max_consecutives.py)
- [Find Number with even number of Digits](../ProblemsAndSolutions/even_no_digit.py)
- [Squares of a sorted array](../ProblemsAndSolutions/sorted_array.py)

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

> 

###### I am  welcoming any more optimized solution you have, Make a PR
## we move

see you on <a href="./day06.md">Day 06</a>