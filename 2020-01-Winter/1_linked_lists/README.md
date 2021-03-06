<!-- Don't remove -->
<a name="top"/>

# Linked Lists

Problems and solutions for Linked Lists session on January 24, 2020.

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

### 1. LIST PALINDROME 

Source: geeksforgeeks 

#### Scenario

Check if a linked list of N integers is a palindrome. 

Return 1 if palindrome, 0 otherwise

1 <= n <= 10

#### Example Input

Input: 1->2->1

Output: 1

Input: 1

Output: 0

#### Function Signature

Java:

```
class Node
{
	int data;
	Node next;
	
	Node(int d)
	{
		data = d;
		next = null;
	}
}

boolean isPalindrome(Node head) 
{
    //Your code here
}  
```

C++:

```
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};

bool isPalindrome(Node *head)
{
    //Your code here
}
```
<!-- Don't remove -->
Go to [Solution](#s1)   [Top](#top)


<!-- Don't remove -->
<a name="p2"/>

### 2. PROBLEM 2 TODO :bug:

Source: [LeetCode](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

#### Scenario

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.


#### Example Input

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:

	1---2---3---4---5---6---NULL
		|
		7---8---9---10---NULL
	    	    |
	   	    11--12---NULL


After flattening the multilevel linked list it becomes:

	1---2---3---7---8---11---12---9---10---4---5---6---NULL

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  	1---2---NULL
  	|
  	3---NULL
  
 After flattening the multilevel linked list it becomes:
 
 	 1---3---2---NULL
	 
Example 3:

Input: head = []
Output: []

#### Function Signature

public Node flatten(Node head)

<!-- Don't remove -->
Go to [Solution](#s2)   [Top](#top)

<!-- Don't remove -->
<a name="p3"/>

### 3. Linked List Duplicates

Source: Cracking The Code Interview Book, Chapter 2, Question 2.1

#### Scenario

Remove duplicated from an **unsorted** linked list of integers.
*Follow Up Question:* How would you solve this without a temporary buffer?

**Assume the Tail will NOT connect back to the Head. Meaning it is NOT circular.**

#### Function Signature

```C++
void RemoveDuplicatesWithBuffer(Node *Start);

void RemoveDuplicatesWithoutBuffer(Node *Start)
```

<!-- Don't remove -->
Go to [Solution](#s3)   [Top](#top)

<!-- Don't remove -->
<a name="solutions"/>

## Solutions

<!-- Don't remove -->
<a name="s1"/>

### 1. LIST PALINDROME 

Source: geeksforgeeks 

#### Solution

A simple solution is to use a stack of list nodes.
This mainly involves three steps:
1. Traverse the given list from head to tail and push every visited node to stack.
2. Traverse the list again. For every visited node, pop a node from stack and 
compare data of popped node with currently visited node.
3. If all nodes matched, then return true, else false.

Runtime of this will be O(N)

```java
public static boolean isPalindrome(Node head) 
    {
        //Your code here
        Node current = head; 
        boolean ispalin = true; 
        Stack<Integer> stack = new Stack<Integer>(); 

        if(head.next == null){
            return true;
        }
  
        while (current != null) { 
            stack.push(current.data); 
            current = current.next; 
        } 
  
        while (head != null) { 
  
            int i = stack.pop(); 
            if (head.data == i) { 
                ispalin = true; 
            } 
            else { 
                ispalin = false; 
                break; 
            } 
            head = head.next; 
        } 
        return ispalin;
    }    
```

#### Driver For Solution

The coded solution [is available here.](./list-palindrome/driver.java)

<!-- Don't remove -->
Go to [Top](#top)

<!-- Don't remove -->
<a name="s2"/>

### 2. SOLUTION 2 TODO :bug:

Source: [LeetCode](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

#### Solution
In this solution, you first check the base case that the Linked List you call the flatten method on is not null. If it is you return the empty list. Otherwise you will use the tail node to travel to the tail of the first level of the list. You then begin traversing through the first level of the list until you reach the tail checking each node and whether or not they have a child node and thus another level to the list. If a second level is found move the level below in between current and current.next. Continue this until you have reached the tail node of the list.

```java

	public Node flatten(Node head) {
		/*Base case*/
		if (head == null) { 
			return head; 
		} 

		/* Find tail node of first level linked list */
		Node tail = head; 
		while (tail.next != null) { 
			tail = tail.next; 
		} 

		// One by one traverse through all nodes of first level 
		// linked list till we reach the tail node 
		Node current = head; 
		while (current != null) { 
			

			// If current node has a child 
			if (current.child != null) { 
				// then link child in between current and current.next
				//store last link on next level as temp to connect to
				//current.next
				Node temp = current.child; 
				while (temp.next != null) { 
					temp = temp.next; 
				} 
				//break and create new links
				temp.next = current.next;
				if(current.next != null){
					current.next.prev = temp;
				}
				current.next = current.child; 
				current.child.prev = current;
				current.child = null;
			} 

			// Change current node 
			current = current.next; 
		} 
		return head;
	}
```

#### Driver For Solution

[Driver](CTCI/2020-01-Winter/1_linked_lists/Flatten_Multilevel_Doubly_Linked_List/LinkedList.java)

<!-- Don't remove -->
Go to [Top](#top)

<!-- Don't remove -->
<a name="s3"/>

### 3. SOLUTION 3

Source: Cracking the Code Interview Book, Chapter 2, Question 2.1

#### Solution 

With the Buffer: Use a set to keep track of what integers have been encountered.
This solution is O(n) because it iterates over the list one time, and the `unordered_set` has a O(1) efficiency.

```C++
void RemoveDuplicatesWithBuffer(Node *Start) {
  if (Start == nullptr || Start->GetNext() == nullptr) {
    return;
  }

  unordered_set<int> set;

  Node *Curr = Start;
  Node *Prev = nullptr;

  while (Curr != nullptr) {
    // Doesn't exist
    if (set.find(Curr->GetValue()) == set.end()) {

      set.insert(Curr->GetValue());
      Prev = Curr;
      Curr = Curr->GetNext();

    } else { // Exists

      Prev->SetNext(Curr->GetNext());
      delete Curr;
      Curr = Prev->GetNext();
    }
  }
}
```

Without a Buffer: Have a pointer/runner that iterates over the list to check for duplicates.
This solution is O(n^2) because it could potentially iterate over the entire list twice checking for duplicates.
Although the time complexity is high, it does not use extra memory.

```C++
void RemoveDuplicatesWithoutBuffer(Node *Start) {
  if (Start == nullptr || Start->GetNext() == nullptr) {
    return;
  }

  Node *Prev = Start;
  Node *Curr = Prev->GetNext();

  while (Curr != nullptr) {

    Node *Check = Start;

    while (Check != Curr) { // Check for earlier duplicates

      if (Check->GetValue() == Curr->GetValue()) {
        Prev->SetNext(Curr->GetNext());
        Curr = Curr->GetNext();
        break; // All other duplicates have been removed
      }
      Check = Check->GetNext();
    }
    if (Check == Curr) { // Update the current
      Prev = Curr;
      Curr = Curr->GetNext();
    }
  }
}
```

#### Testing The Solutions OR Driver For Solution

Write your code in the `main.cpp` file, the tests are located at the bottom of the file.

<!-- Don't remove -->
Go to [Top](#top)
