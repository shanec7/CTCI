<!-- Don't remove -->
<a name="top"/>

# Topic Name TODO :bug:

Simple description TODO :bug:

In the style of:
***Problems and solutions for Maze & Dynamic Programming session on March 1, 2019.***

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

### 1. PROBLEM 1 TODO :bug:

Source: TODO :bug:

#### Scenario

Problem Statement TODO :bug:

#### Example Input

If the problem is simple enough, remove this section. TODO :bug:

#### Function Signature

TODO :bug:

<!-- Don't remove -->
Go to [Solution](#s1)   [Top](#top)

<!-- Don't remove -->
<a name="p2"/>

### 2. Find the Town Judge

Source: [LeetCode](https://leetcode.com/problems/find-the-town-judge/)

#### Scenario

In a town, there are `N` people labelled from `1` to `N`.  There is a rumor that one 
of these people is secretly the town judge.

If the town judge exists, then:

1.  The town judge trusts nobody.
2.  Everybody (except for the town judge) trusts the town judge.
3.  There is ***exactly one*** person that satisfies properties 1 and 2.

You are given `trust`, an array of pairs `trust[i] = (a, b)` representing that person `a` trusts person `b`.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return `-1`.

#### Example Input

```
Input: N = 2, trust = [[1,2]]
Output: 2
```

```
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

#### Function Signature

Java:

```java
int findJudge(int N, int[][] trust) {
    // your code here
}
```

C++:
```c++
int findJudge(int N, vector<vector<int>>& trust) {
    // your code here
}
```

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

### 1. SOLUTION 1 TODO :bug:

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
<a name="s2"/>

### 2. Find the Town Judge

Source: [LeetCode](https://leetcode.com/problems/find-the-town-judge/)

#### Solution

Solution in Python:

```python3
def find_judge(N: int, trust: list):
    # Edge case: if there are no trust pairs,
    # N has to be 1 to satisfy the rules (judging him/herself)
    if len(trust) == 0:
        return 1 if N == 1 else -1
    
    trust_vals = defaultdict(int)
    
    # trust someone else == give out 1 trust_val
    # being trusted == receive 1 trust_val
    for from_person, to_person in trust:
        trust_vals[from_person] -= 1
        trust_vals[to_person] += 1
        
    # find the judge
    for person, trust_val in trust_vals.items():
        # judge trusts no one (-0), and is trusted by everyone else (+N-1)
        if trust_val == N - 1:
            return person
        
    # there is no judge
    return -1
```

#### Driver For Solution

The Python solution is [here](./town_judge/town_judge.py]).

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
