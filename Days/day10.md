## Big O Analysis in everyday code

This section is not about the code. More about the Big-O analogy

- [Explainer and expression in Big0](#explainer-and-expression-in-big0)
- [Q1 - Mean Average of Even Numbers](#q1---mean-average-of-even-numbers)
      - [breakdown](#breakdown)
- [Q2 - Word Builder](#q2---word-builder)
      - [breakdown](#breakdown-1)
- [Q3 - Array Sample](#q3---array-sample)
      - [breakdown](#breakdown-2)
- [Q4 - Average Celsius Reading](#q4---average-celsius-reading)
      - [breakdown](#breakdown-3)
- [Q5 - Clothing Labels](#q5---clothing-labels)
    - [breakdown](#breakdown-4)
- [Q6 - Count the Ones](#q6---count-the-ones)
    - [breakdown](#breakdown-5)
- [Q7 - Dealing with multiple Dataset](#q7---dealing-with-multiple-dataset)
    - [breakdown](#breakdown-6)
- [we move](#we-move)

# Explainer and expression in Big0

With Big O Notation, we have a consistent system  that allows us to compare any two algorithms. With it, we will be able to determine our code efficiency and performance.
# Q1 - Mean Average of Even Numbers

> Function that accept an array of numbers and returns the mean average of all its even numbers. How would you express in terms of BigO

```
def average_of_even_number(array):
  # The mean average of even numbers will be defined as the sum of the even numbers divided by the count of even  numbers, so we keep track of both teh sum and the count
  total_sum = 0
  count = 0
  # we iterate through each number in the array, and if we emcounter an even number, we modify the sum and the count:
  for number in array:
    if number %2 ==0:
      total_sum += number
      count +=1
  return total_sum / count_of_even_numbers
```

#### breakdown

Big O is all about answering the key question: if there  are N data elements, how many steps will the algorithmes takes? Therefore, the first thing we want to do is determine what "N" elements are:

in our case, the algorithms is processing the array of numers passed into the method. These, then would be the "N" data elements, with N being the size of the array.

Next we determine the number of step the algorithm take to process these N values.

we can see that the guts of the algorithm is the loop the iterate over each number inside the array, so we'll want to analyze that first and since the loop iterate over each of the N elements, we know that the algorithms takes at least N steps.

Big O focusses on the worst case scenarios. In our case, the worst case is when all the numbers are even, in which case, we perform three step during each round of the loop. hence 3N. Additional steps outside the loop(setting two varibles and division of sum with count), i.e 3N + 3. However Big 0 drops constants.

O(3N+3) -> O(N)

# Q2 - Word Builder

> Function that collects every combination of two-character strings built  from an array of single characters. e.g Array ["a","b","c","d"], we'd return a new array containing the following strings
> [
> 'ab', 'ac', 'ad','ba','bc','bd','ca','cb','cd','da','db','dc'
>]

```
  def wordBuilder(array):
    let collection= []
    for i in range(len(array)):
      for j in range(len(array)):
        if(i != j):
          collection.append(array[i] + array[j])
    return collection
```

#### breakdown

Herw we are running one loop nested inside another. The outer loop iterate each character in the array, keeping track of the index i. For each index i, we run an inner loop that iterates again over each character in the same array using the index j, within this inner loop, we concatenate the character at i and j, with the exception of when i and j are pointing at the same index.

To determine the algorithm efficiency, we once again need to determine what the N data elements are. In our case, as in the previous example. N is the number of element inside the array passed to the function.

Next, determine the number of step our algorithm takes relative to the N elements. In our case, the outer loop iterates over all N elements and for each element, the outer loop iterates again over all N elements, which amounts to N steps multiplied by N steps. This is the classic cause of O(N^2) and it what nested loop algorithm turn out to be but be careful as this is not a general true.

# Q3 - Array Sample

>Function that takes an array and return its first, middle and last value.

```
def sample(array):
  first = array[0]
  middle = array[int(len(array) // 2)]
  last = array[-1]

  return  [first, middle, last]
```

#### breakdown

Here, the data passed into the array is the primary data. so we can say N is the number of elements in the array.

However,our function ends p taking the same number of steps no matter what N is. Reading from the beginning, midpoint and last indexes of an array each takes one step no matter the size of the array. Similarly, finding the array's length and dividing it bby 2 also takes one step.

Since the step is CONSTANT - that is, it remain the same no matter what N is- this algorithm is considered O(1).

# Q4 - Average Celsius Reading
>Let's say we are building a weather forecasting software. To determine the temperature of a city, we take temperature readings from across many thermometers across the city, and we calculate the mean average of those temperatures/

```
def average_celsius(fahrenheit_readings):
  # Collect Celsius numbers here
  celsius_number = []
  # convert each reading to celsius and add to array
  for reading in fahrenheit_readings:
    celsius_conversion = (reading - 32) / 1.8
    celsius_number.append(celsius_conversion)
  
  sum_ = 0

  for celsius_num in celsius_number:
    sum_ += celsius_num

  return sum_ / len(celsius_number)

```

#### breakdown

First, we can say that N is the number of fahrenheit_readings passed into the function.

Inside, we have two loops, one converts the readings to Celsius and the second sums all the celsius number. Since we have two loops that each iterate over all the N element, we have N + N, which is 2N (plus a few constant steps). Recall Big O drops constants, hence O(N).

Do not get thrown off by the two loops. They are not nested.

# Q5 - Clothing Labels
>We are writing a software for a a clothing manufacturer, our code accepts an array of newly produced clothing (stored as a string), and creates text for possible labels we'll need.]
e.g  ["Purple SHort","Green Shirt"]
> Output -[
>   "Purple Shirt Size: 1",
> "Purple Shirt Size: 2",
> "Purple Shirt Size: 3",
> "Purple Shirt Size: 4",
> "Purple Shirt Size: 5",
> "Green Shirt Size: 1",
> "Green Shirt Size: 2",
> "Green Shirt Size: 3",
> "Green Shirt Size: 4",
> "Green Shirt Size: 5",
> ]

```
def mark_inventory|(clothing_items):
  clothing_options =[]

  for item in clothing_items:
    #for sizes i through 5 (python ranges go UP to second number but not included)
    for size in range(1,6):
      clothing_options.append(item + ' Size: ' " str(size))
  return clothing_options
```

### breakdown

It is safe to say =, N is the number of clothing_items/

This code contains nested loop, so it is tempting to declare it O(N^2). However, we need to analyze this case closely.

Nested loops that reult in O(N^2) occur when each loop revolves around N. In our case, however, while our outer loop runs N times, our inner loops runs at constant times. i.e , this inner loop will always run fie times no matter what. Hence O(N)

# Q6 - Count the Ones
>Function accepts an array of arrays, where the inner arrays contain 1's and 0's. The function then return how many 1's there are. e.g the input 
>[
>[0,1,1,1,0],
>[0,1,0,1,0,0,1,1,1]
>[1,0]
>]


```
def count_ones(outer_array):
  count = 0
  for inner_array in outer_array:
    for num in inner_array:
      if num ==1:
        count +=1
  return count
```

### breakdown

Again, it is easy to notice the nested loops and jump to the conclusion that is is O(N^2). However, the two loops are iterating over two completely different things/

The outer loop is iterating over the inner arrays and the inner is iterating over the actual number. At the end if the day our inner loops only runs for as  mant numbers as there are in total.

Hence O(N)

# Q7 - Dealing with multiple Dataset
> What happen if we compute the product of every number from one array by every number of a second array ?, e.g if we had array [1,2,3] and the array [10,100,1000]. we would compute the products as:
> [10,100,1000,20,200,2000,30,300,3000]

```
  def twoNumberProduct(array1, array2){
    let product=[]

    for i in range(len(array1)):
      for j in range(len(array2)):
        products.append(array1[i]*array2[j]) 
    return products
  }
```

### breakdown

Let's analyze the time complexity of this algorithm. First, what is N? This is the first huddle, as we  now have two datasets namely, the two arrays.

It's tempting to lump everything together and say the N is the total number of items of both array. However, this is problematic for the following reasons:

Here is a tale of two case. In case 1, there are two array of size 5. In case 2, there are one array of ize 9 and another of size 1.

In both, we'd end up saying that N is 10, since 5+5 =10 and 9+1 =10. However, the efficiency of both case is very different.

In case 1, our code takes 25(25*5) steps, because N is 10. This is equivalent to (N/2)^2 steps.

In case 2, our code takes 9(9*1) steps, which is close to about N steps. This is dramatically faster than case 2.

SO, we do not want to consider N to be the total number of integers from bth arrays, since we would never be able to pin down the efficiency in terms of BigO Notations. as it varies based on the different cases.
We are in a bit of a bind here. We have no choice but to express the time complexity as O(N*M), where N is the size of one array and M is the size of another.

This is the new concept, whenever we have two distinct datasets that have to interact with each other through multiplication, we have to identify both sources separately when we describe the efficiency in terms of Big O

# we move

see you on <a href="./day11.md">Day 11</a>
