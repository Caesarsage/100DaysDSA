# Recursively Recurse with Recursion

Recursion is a key concept in computer science that will unblock th e more adanced algorithms we are going to encounter in this book.

```function blah() {
  blah()
}
```
****
Recursion is a function that call itself. Of course, infinite recursion is utterly useless as in above. When harnessed correctly, though. recursion can be a powerful tool.

## Recurse instead of Loop

Say you design a countDown from number to zero

```
function countDown(num) {
  for(i=num, i >= 0; i--) {
    console.log(i)
  }
}

countDown(10)
```

There is nothing wrong with the program above but it might needed occur to you that you do not have to use loop.

```
function countDown(num) {
  
  if (num == 0 ) return 0
  if (num == 1) return 1

  console.log(num)

  return countDown(num-1)
}
```

The case in which our function will not recurse is known as the *base case*. so 0 and 1 is the base case for our countDown() function.

