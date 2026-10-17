'''
Graphs DFS + BFS

A graph is a data structure made up of nodes (vertices)
and edges (connections between nodes).

GRAPH REPRESENTATIONS
--------------------------------------------------
Graphs can be represented in several ways:

1. 2D Grid (Matrix)
   - Each cell acts as a node.
   - Cells are typically connected up, down, left, and right.
   - Common in island, maze, and flood fill problems.

2. Adjacency List
   - Each node stores a list of its neighbors.
   - Common in network and general graph problems.


DEPTH-FIRST SEARCH (DFS)
--------------------------------------------------
DFS is an algorithm used to traverse or explore graphs.

The idea:
- Start at a node.
- Explore one path as deeply as possible.
- When you can't go further, backtrack.
- Continue exploring other paths.

DFS typically uses recursion or a stack.

Example:

       A
      / \
     B   C
    / \
   D   E

Possible DFS traversal:
A -> B -> D -> E -> C


DFS ON A 2D GRID
--------------------------------------------------
For grid problems, each cell is treated like a node.

We typically explore four directions:
- Up:    (r - 1, c)
- Down:  (r + 1, c)
- Left:  (r, c - 1)
- Right: (r, c + 1)

DFS steps:
1. Check the base case (out of bounds, invalid, or visited).
2. Mark the current cell as visited.
3. Recursively explore neighboring cells.
4. Return a result if the problem requires one.

Time Complexity: O(R * C)
- In the worst case, we visit every cell once.

Space Complexity: O(R * C)
- The recursion stack can contain up to R * C cells.


PRACTICE PROBLEMS
--------------------------------------------------

1) Count Unique Paths in a Grid

You are given an m x n binary matrix grid, where:
- 0 represents an empty cell that you can walk through.
- 1 represents an obstacle that you cannot walk through.
You start at the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1).
You may move in four directions: up, down, left, or right.
You cannot visit the same cell more than once in a single path.
Return the total number of unique valid paths from the starting cell to the destination.

class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        pass
        

2) Word Search (79)
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


'''