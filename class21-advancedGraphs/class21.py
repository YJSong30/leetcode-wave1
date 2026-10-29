'''
ADVANCED GRAPHS
==================================================

Two important graph algorithms:
1. Dijkstra's Algorithm - Shortest path
2. Topological Sort - Dependency ordering

Both commonly use adjacency lists to represent graphs.


DIJKSTRA'S ALGORITHM
==================================================
Purpose:
- Finds the shortest distance from a starting node
  to every other reachable node.
- Works with weighted graphs (nonnegative weights).
- Uses an adjacency list, distance array, and min-heap.

Common keywords:
- Shortest path
- Minimum cost
- Minimum travel time
- Weighted graph

Step 1: Build the adjacency list
--------------------------------------------------
Each connection has a destination and weight.

times = [
    [1, 2, 5],
    [1, 3, 2],
    [3, 2, 1]
]

Each entry represents [source, destination, weight].

adj_list = {
    1: [(2, 5), (3, 2)],
    3: [(2, 1)]
}

Read 1: [(2, 5), (3, 2)] as:
- Node 1 connects to Node 2 with cost 5.
- Node 1 connects to Node 3 with cost 2.


Step 2: Initialize distances
--------------------------------------------------
- Set every node's distance to infinity.
- Set the starting node's distance to 0.

dist = [float('inf')] * (n + 1)
dist[k] = 0

The distance array stores the shortest distance
discovered so far from the starting node.


Step 3: Initialize the min-heap
--------------------------------------------------
heap = [(0, k)]

Each tuple stores (distance, node).

The min-heap prioritizes the smallest distance.


Step 4: Process the heap
--------------------------------------------------
1. Pop the node with the smallest distance.
2. Skip it if its distance is outdated.
3. Explore its neighbors using the adjacency list.
4. Calculate the new distance to each neighbor.
5. If the new distance is smaller, update dist.
6. Push the updated distance and node into the heap.
7. Repeat until the heap is empty.

Core logic:

while heap:
    curr_dist, node = heapq.heappop(heap)

    if curr_dist > dist[node]:
        continue

    for nei, weight in adj_list[node]:
        new_dist = curr_dist + weight

        if new_dist < dist[nei]:
            dist[nei] = new_dist
            heapq.heappush(heap, (new_dist, nei))

Important:
- The heap determines which node to explore next.
- The dist array remembers the best distance found.
- The heap may contain outdated distances.
- heappush() and heappop() take O(log H),
  where H is the current heap size.

Time: O((V + E) log V) for a simple graph
Space: O(V + E)

V = Number of vertices (nodes)
E = Number of edges (connections)

Practice:
743. Network Delay Time


TOPOLOGICAL SORT / KAHN'S ALGORITHM (BFS)
==================================================
Purpose:
- Determines a valid order to complete tasks
  that have dependencies.
- Can detect whether a directed graph has a cycle.
- Uses an adjacency list, indegree array, and queue.
- A valid topological ordering requires a
  Directed Acyclic Graph (DAG).

Common keywords:
- Prerequisites
- Dependencies
- Course schedule
- Task ordering
- Can all tasks be completed?

Unlike regular BFS, we aren't checking whether
nodes are reachable. We're checking whether
all dependencies can be satisfied.


Step 1: Build the adjacency list
--------------------------------------------------
Example:

numCourses = 4

prerequisites = [
    [1, 0],
    [2, 0],
    [3, 1],
    [3, 2]
]

Each pair is [course, prerequisite].

[1, 0] means Course 0 must be completed
before Course 1.

adj_list = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

Read 0: [1, 2] as:
- Course 0 must come before Courses 1 and 2.

The graph is DIRECTED.
Do not add reverse edges.


Step 2: Build the indegree array
--------------------------------------------------
Indegree = number of incoming edges to a node.

For Course Schedule, it represents the number
of prerequisites a course still needs.

indegree = [0, 1, 1, 2]

Course 0: 0 prerequisites
Course 1: 1 prerequisite
Course 2: 1 prerequisite
Course 3: 2 prerequisites

When building the graph:

for course, pre in prerequisites:
    adj_list[pre].append(course)
    indegree[course] += 1


Step 3: Initialize the BFS queue
--------------------------------------------------
Add ALL nodes with indegree 0 to the queue.

These courses can be completed immediately.

q = deque()

for i in range(numCourses):
    if indegree[i] == 0:
        q.append(i)

Example:
indegree = [0, 1, 1, 2]

q = deque([0])

Important:
- We don't always start at Node 0.
- We start with every node whose indegree is 0.


Step 4: Process courses using BFS
--------------------------------------------------
1. Pop a course from the queue.
2. Mark that course completed.
3. Find courses that depend on it.
4. Decrease their remaining indegrees by 1.
5. If a neighbor's indegree reaches 0,
   add it to the queue.
6. Repeat until the queue is empty.

Core logic:

count = 0

while q:
    node = q.popleft()
    count += 1

    for nei in adj_list[node]:
        indegree[nei] -= 1

        if indegree[nei] == 0:
            q.append(nei)


Step 5: Example walkthrough
--------------------------------------------------
Initial:
indegree = [0, 1, 1, 2]
queue = [0]
count = 0

Process Course 0:
- count = 1
- Reduce indegree of Courses 1 and 2.
- Both reach 0, so enqueue them.

queue = [1, 2]
indegree = [0, 0, 0, 2]

Process Course 1:
- count = 2
- Reduce Course 3's indegree from 2 to 1.
- Course 3 is not ready yet.

queue = [2]
indegree = [0, 0, 0, 1]

Process Course 2:
- count = 3
- Reduce Course 3's indegree from 1 to 0.
- Add Course 3 to the queue.

queue = [3]
indegree = [0, 0, 0, 0]

Process Course 3:
- count = 4
- No more neighbors.

queue = []

All 4 courses were completed.


Step 6: Check for cycles
--------------------------------------------------
If count == numCourses:
- All courses were completed.
- No directed cycles exist.
- Return True.

If count < numCourses:
- Some courses could not be completed.
- A directed cycle exists.
- Return False.

return count == numCourses

Why?
A cycle creates circular dependencies.

Example:
0 -> 1 -> 2 -> 0

Every node depends on another node.
No node in the cycle can reach indegree 0.


Step 7: Course Schedule I vs II
--------------------------------------------------
207. Course Schedule:
- Return True or False.
- Use count to track completed courses.

210. Course Schedule II:
- Return a valid course order.
- Use res.append(node) instead of count += 1.
- Return res if len(res) == numCourses.
- Otherwise return [].


TIME AND SPACE COMPLEXITY
--------------------------------------------------
Time: O(V + E)
- O(V) to initialize indegrees and the queue.
- O(E) to build the graph.
- Each node is processed once.
- Each edge is examined once.

Space: O(V + E)
- Adjacency list: O(V + E) generally.
- Indegree array: O(V).
- Queue: O(V).

No min-heap is needed, so no log V factor.


DIJKSTRA VS TOPOLOGICAL SORT
==================================================

Dijkstra:
- Finds shortest distances.
- Uses weighted edges.
- Uses a min-heap.
- Time: O((V + E) log V) for simple graphs.

Topological Sort:
- Finds a valid dependency order.
- Uses directed edges.
- Uses indegrees and a queue.
- Time: O(V + E).

KEY TAKEAWAYS
==================================================
Dijkstra:
Heap = Which node has the smallest distance?
Dist = What's the best distance found so far?

Topological Sort:
Indegree = How many prerequisites remain?
Queue = Which courses are ready?
Count = How many courses have been completed?

Dijkstra finds the cheapest path.
Topological Sort finds a valid order.

743) Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for src, dst, weight in times:
            adj_list[src].append((dst, weight))

        print(adj_list)
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        print(dist)
        heap = [(0, k)] # (distance, starting_node)

        while heap:
            curr_dist, src = heapq.heappop(heap)

            # skip outdated distances
            if curr_dist > dist[src]:
                continue

            for nei, w2 in adj_list[src]:
                new_dist = curr_dist + w2
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        if max(dist[1:]) == float('inf'):
            return -1

        return max(dist[1:])

207) Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for dst, src in prerequisites:
            adj_list[src].append(dst)
            in_degree[dst] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        count = 0

        while queue:
            count += 1
            node = queue.popleft()

            for nei in adj_list[node]:
                in_degree[nei] -= 1

                if in_degree[nei] == 0:
                    queue.append(nei)

        return count == numCourses
'''