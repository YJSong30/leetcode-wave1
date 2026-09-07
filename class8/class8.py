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
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

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
'''