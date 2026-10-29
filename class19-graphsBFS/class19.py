'''
Graphs BREADTH-FIRST SEARCH (BFS)

--------------------------------------------------
BFS is an algorithm used to traverse or explore graphs.

Unlike DFS, which explores one path deeply before backtracking, BFS explores nodes level by level.

BFS uses a queue (FIFO - First In, First Out).

How BFS works:
1. Add the starting node to the queue.
2. Mark the starting node as visited.
3. Remove the first node from the queue.
4. Explore its neighboring nodes.
5. Add unvisited neighbors to the queue and mark them visited.
6. Repeat until the queue is empty.


BFS ON A 2D GRID
--------------------------------------------------
Each cell represents a node, and neighboring cells
are connected.

We typically explore four directions:
- Down:  (r + 1, c)
- Up:    (r - 1, c)
- Right: (r, c + 1)
- Left:  (r, c - 1)

We use collections.deque for the queue:
- q.append()  -> Add to the back of the queue.
- q.popleft() -> Remove from the front of the queue.

Visited:
- Prevents processing the same cell multiple times.
- Mark cells visited BEFORE adding them to the queue.
- Can use a visited set or modify the grid directly.


BFS LEVELS
--------------------------------------------------
BFS explores nodes in layers based on their distance
from the starting node.

Level 0: Starting node
Level 1: Immediate neighbors
Level 2: Neighbors of level 1
Level 3: Neighbors of level 2

Use for _ in range(len(q)) to process one entire level.

Each iteration of the outer while loop processes
the next level.

This is useful when counting:
- Minimum steps
- Shortest distance
- Minutes or time elapsed

If we only need to explore connected cells, we don't need to track levels.


SINGLE-SOURCE VS MULTI-SOURCE BFS
--------------------------------------------------
Single-source BFS:
- Start from one node or cell.
- Example: Flood Fill.

Multi-source BFS:
- Start from multiple nodes simultaneously.
- Add all starting nodes to the queue initially.
- Example: Rotting Oranges.


WHEN TO USE BFS
--------------------------------------------------
Common keywords:
- Shortest path (unweighted graph)
- Minimum steps or moves
- Nearest or closest node
- Minimum time or minutes
- Spread or infection
- Level-by-level traversal
- Explore connected regions

BFS vs DFS:
- BFS: Queue, explores level by level.
- DFS: Recursion/stack, explores deeply first.
- Both can explore connected regions.
- BFS is preferred for shortest paths in unweighted graphs.
- DFS is often preferred for backtracking problems.


TIME AND SPACE COMPLEXITY
--------------------------------------------------
For a 2D grid with R rows and C columns:

Time: O(R * C)
- Each cell is visited at most once.
- Each cell checks up to 4 neighbors.

Space: O(R * C)
- The queue and visited set may store many cells.

For a general graph with V vertices and E edges:

Time: O(V + E)
Space: O(V)

These assume standard BFS that marks nodes visited.
'''

'''
1) Flood Fill

You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        if image[sr][sc] == color:
            return image

        q = deque([(sr, sc)])
        image[sr][sc] = color

        while q:
            r, c = q.popleft()

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if min(nr, nc) < 0 or nc == cols or nr == rows or image[nr][nc] != original_color:
                    continue

                image[nr][nc] = color
                q.append((nr, nc))

        return image


2) Rotting Oranges
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        num_fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    num_fresh += 1
        
        if num_fresh == 0:
            return 0
        
        time = -1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while queue:
            queue_len = len(queue)
            time += 1
            for i in range(queue_len):
                r, c = queue.popleft()

                for j, k in directions:
                    dr = r + j
                    dc = c + k

                    if min(dr,dc) < 0 or dr == rows or dc == cols or grid[dr][dc] == 0 or grid[dr][dc] == 2:
                        continue

                    grid[dr][dc] = 2
                    num_fresh -= 1
                    queue.append((dr, dc))
        
        if num_fresh > 0:
            return -1
        else:
            return time

'''