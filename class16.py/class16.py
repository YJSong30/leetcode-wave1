'''
Heap

- A heap is a tree-based data structure designed to quickly retrieve the smallest or largest element.
- in Python, we typically use heapq, which implements a min-heap.
- use when you repeatedly need the smallest, largest, earliest, or highest-priority element.

see heapq.png

- min-heap: parent <= children
- max-heap: parent >= children

A heap is not completely sorted. It only guarantees the parent-child relationship.

Ex: heap = [1, 3, 2, 7, 5, 4, 6]

parent = (i - 1) // 2
left_child = 2i + 1
right_child = 2i + 2

Heappop steps:

1. Save the root (minimum).
2. Remove the last element and put it at the root.
3. Compare the new root with its children.
4. Swap with the smaller child if needed.
5. Repeat until the heap property is restored.
6. Return the original root.
Time complexity: O(log n) — because you only sift down one path through the tree, not sort the entire heap


1) Implement heapq ourselves:

class MinHeap:
    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

h = MinHeap()
for x in [1, 3, 2, 7, 5, 8, 4]:
    h.push(x)

print(h.heap)  # [1, 3, 2, 7, 5, 8, 4]
print(h.pop()) # 1
print(h.heap)  # [2, 3, 4, 7, 5, 8]


347) Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass
        

'''