'''
Linked List

1. What is a Linked List?

With a normal Python list:
nums = [10, 20, 30]
you can think of the values as sitting next to each other.

A linked list works differently.
Each object stores: value + where the next node is

Example:
10 → 20 → 30 → None

Each individual item is called a node.

2. Node
Typical LeetCode node:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

Each node contains:
- node.val (the value) and node.next (the next node)

Example:
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3

node1 -> node2 -> node3

3. head

You'll constantly see keyword "head"
head is simply: the first node of the linked list.
Example:

head
 ↓
10 → 20 → 30 → None

So: 
- head.val => 10
- head.next.val => 20

4. Traversing a Linked List

With an array:

for num in nums:

With a linked list, you usually do:

current = head

while current:
    print(current.val)
    current = current.next

Example:

10 → 20 → 30 → None

Execution:

current = 10
current = 20
current = 30
current = None

Then stop.

This pattern is extremely important:

current = head

while current:
    current = current.next

You'll use it constantly.

5. Why can't we use head[2]?

Arrays support indexing:

nums[2]

Linked lists don't.

To reach the third node:

10 → 20 → 30

you have to follow:

head.next.next

So accessing the nth element is:

O(n)

instead of array:

O(1)
6. Linked List Operations
Read first node
head.val
O(1)
Find something
current = head

while current:
    if current.val == target:
        return True

    current = current.next
O(n)
Insert at beginning

Suppose:

10 → 20 → 30

We want:

5 → 10 → 20 → 30

Do:

newNode = ListNode(5)

newNode.next = head
head = newNode

That's:

O(1)
7. The biggest linked-list concept

You are usually not moving values around.

You are changing:

.next

references.

For example:

node.next = something

You're saying:

after this node, go to this other node.

That's basically the entire foundation of linked lists.

8. Common Variables

You'll see these constantly:

head
current
prev
nextNode
slow
fast
dummy
current

Node you're currently looking at.

current = head
prev

Previous node.

Very useful when reversing lists.

nextNode

Save the next node before changing pointers.

slow / fast

Used for:

finding middle
detecting cycles
dummy

Fake node placed before the head.

Makes edge cases much easier.

Example:

dummy → 1 → 2 → 3
'''