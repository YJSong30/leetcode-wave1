'''
Breadth First Search

BFS stands for Breadth-First Search.

BFS explores a tree level by level.

Example:

        1
       / \
      2   3
     / \
    4   5

BFS visits:

1
2 3
4 5

So the order is:

1 → 2 → 3 → 4 → 5

DFS goes deep first.
BFS finishes the current level before moving to the next level.
BFS uses a queue.

A queue follows: FIFO = First In, First Out

In Python, we usually use:
from collections import deque

Create a queue:
queue = deque()

Add something to the back:
queue.append(value)

Remove something from the front:
queue.popleft()

def bfs(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


102) Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        pass


199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        pass


'''