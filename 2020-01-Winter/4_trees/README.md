<!-- Don't remove -->
<a name="top"/>

# Trees

Problems and solutions for Trees session on February 14, 2020.

### Table of Contents

* [Problems](#problems)
  * [1](#p1)
  * [2](#p2)
  * [3](#p3)
* [Solutions](#solutions)
  * [1](#s1)
  * [2](#s2)
  * [3](#s3)

<!-- Don't remove -->
<a name="problems"/>

## Problems

<a name="p1"/>

### 1. Fibonacci

Source: [GeeksForGeeks](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/)

#### Scenario

Given an integer `n`, find the `n`th term of the Fibonacci sequence.

#### Example Input

If the sequence starts as `0, 1, 1, 2, 3, 5, 8, 13, 21`, I should get the following output:

```
Input: n = 1    Output: 0
Input: n = 4    Output: 2
Input: n = -1   Output: 0
```

#### Function Signature

C++:

```c++
int fibonacci(int n) {
    // your code here
}
```

Python:

```python
def fibonacci(n):
    # your code here
```

<!-- Don't remove -->
Go to [Solution](#s1)   [Top](#top)

<!-- Don't remove -->
<a name="p2"/>

### 2. PROBLEM 2 TODO :bug:

Source: TODO :bug:

#### Scenario

Problem Statement TODO :bug:

#### Example Input

If the problem is simple enough, remove this section. TODO :bug:

#### Function Signature

TODO :bug:

<!-- Don't remove -->
Go to [Solution](#s2)   [Top](#top)

<!-- Don't remove -->
<a name="p3"/>

### 3. PROBLEM 3 TODO :bug:

Source: TODO :bug:

#### Scenario

Problem Statement TODO :bug:

#### Example Input

If the problem is simple enough, remove this section. TODO :bug:

#### Function Signature

TODO :bug:

<!-- Don't remove -->
Go to [Solution](#s3)   [Top](#top)

<!-- Don't remove -->
<a name="solutions"/>

## Solutions

<!-- Don't remove -->
<a name="s1"/>

### 1. Fibonacci

Source: [GeeksForGeeks](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/)

#### Solution

We can calculate the `n`th term of the Fibonacci sequence by establishing 
the first two numbers in the sequence as base cases.

The first term is 0; the second term is 1. So, if n <= 1, we know the 
value should be 0. Likewise, if n == 2, we know the value is 1.

We establish a recursive call which takes the sum of the two previous 
terms in the sequence; the recursive implementation is as follows:

```python3
def fib(n):
    if n < 2: return 0
    if n == 2: return 1
    return fib(n - 1) + fib(n - 2)
```

#### Driver For Solution

The solution code is [in the repository](https://github.com/UWB-ACM/CTCI/2020-01-Winter/4_trees/fibonacci/fib.py).

It produces the following output:

```console
$ python3 fib.py
Testing for Nth term of Fibonacci sequence.
N = 0:  0
N = 5:  3
```

<!-- Don't remove -->
Go to [Top](#top)

<!-- Don't remove -->
<a name="s2"/>

### 2. SOLUTION 2 TODO :bug:

Source: TODO :bug:

#### Naive/Simple Solution

TODO :bug:

#### Optimal Solution

TODO :bug:

#### Testing The Solutions OR Driver For Solution

TODO :bug:

<!-- Don't remove -->
Go to [Top](#top)

<!-- Don't remove -->
<a name="s3"/>

### 3. SOLUTION 3 TODO :bug:

Source: TODO :bug:

#### Naive/Simple Solution 

TODO :bug:

#### Optimal Solution

TODO :bug:

#### Testing The Solutions OR Driver For Solution

TODO :bug:

<!-- Don't remove -->
Go to [Top](#top)
