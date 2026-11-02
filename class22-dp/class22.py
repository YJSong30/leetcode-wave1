'''
DYNAMIC PROGRAMMING
==================================================

algorithm used to solve complex problems by breaking them into smaller,
overlapping subproblems and storing their results to avoid repeated calculations.

Instead of solving the same subproblem repeatedly, we store its result and reuse it.

example: fibonacci

Two types of dp:

- Top-Down (Memoization): Start with the original problem, 
recursively break it into smaller subproblems, 
and cache the results so you don't recompute them.

- Bottom-Up (Tabulation): Start with the smallest base cases 
and iteratively build up to the final answer using a DP table.

Both approaches use previously calculated results to avoid repeated work.

Common keywords:
- Maximum / Minimum
- Number of ways
- Can you reach a target?
- Longest / Shortest
- Optimal solution
- Choices at each step

UNDERSTANDING DYNAMIC PROGRAMMING
==================================================

Before writing a DP solution, identify three things:

- State: What does dp[i] represent?
- Transition: How do we calculate the current state using previous states?
- Base Case: What are the smallest subproblems we already know the answers to?


1. MEMOIZATION (TOP-DOWN DP)
==================================================

Purpose:

Starts with the original problem.

Recursively breaks it into smaller subproblems.

Stores calculated results in a cache.

Avoids recalculating previously solved subproblems.

Common keywords:

Recursion

Cache

Previously calculated result

Top-down approach

Step 1: Identify the recursive relationship
Example:


python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
The problem:

fib(5) calls fib(4) and fib(3).

fib(4) also calls fib(3) and fib(2).

fib(3) gets calculated multiple times.

This creates redundant work.

Step 2: Add a cache
Use a dictionary to store previously calculated results.


python
memo = {}

def fib(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]
Step 3: Understand the process
For fib(5):

Calculate fib(5).

Recursively calculate smaller Fibonacci numbers.

Store each calculated result in memo.

If a value already exists, return it immediately.

Avoid repeating calculations.

Important:

Recursion breaks the problem down.

The cache remembers previous answers.

The base case stops the recursion.

Memoization only calculates states that are actually needed.

Complexity
Time: O(n)

Space: O(n)

Cache stores up to n results.

Recursion stack can reach O(n).

2. TABULATION (BOTTOM-UP DP)
==================================================

Purpose:

Starts with the smallest subproblems.

Uses an array to store calculated results.

Builds toward the original problem.

Usually uses iteration instead of recursion.

Common keywords:

DP array

Iteration

Previous states

Bottom-up approach

Step 1: Initialize the DP array
For Fibonacci:


python
n = 5

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1
Each index represents a Fibonacci number.

Meaning:

dp[0] = Fibonacci number at index 0.

dp[1] = Fibonacci number at index 1.

dp[i] = Fibonacci number at index i.

Step 2: Build the DP array
Use the recurrence relationship:

d
p
[
i
]
=
d
p
[
i
−
1
]
+
d
p
[
i
−
2
]
dp[i]=dp[i−1]+dp[i−2]

python
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
Step 3: Return the answer

python
return dp[n]
Example walkthrough:

For n = 5:

Index

Calculation

Value

dp[0]

Base case

0

dp[1]

Base case

1

dp[2]

0 + 1

1

dp[3]

1 + 1

2

dp[4]

2 + 1

3

dp[5]

3 + 2

5

Final DP array:


python
dp = [0, 1, 1, 2, 3, 5]
Important:

Start with known base cases.

Build states in the correct order.

Each state uses previously calculated states.

No recursion is required.

Complexity
Time: O(n)

Space: O(n)

3. MEMOIZATION VS TABULATION
==================================================

Memoization

Tabulation

Top-down

Bottom-up

Uses recursion

Uses iteration

Usually uses a dictionary or cache

Usually uses a DP array

Calculates states when needed

Builds states in order

Uses recursion stack

No recursion stack

Both approaches can solve the same DP problem.

Key takeaway:

Memoization:

Ask: Have I calculated this state before?

If yes, reuse the result.

If no, calculate and store it.

Tabulation:

Start with base cases.

Calculate each state in order.

Return the final answer.

4. HOW TO IDENTIFY A DP PROBLEM
==================================================

Look for these characteristics:

1. Overlapping Subproblems
The same smaller problems are solved multiple times.

Example:

python
fib(5)
    fib(4)
        fib(3)
        fib(2)
    fib(3)
        fib(2)
        fib(1)
Notice fib(3) and fib(2) are calculated repeatedly.

DP stores their answers to avoid repeated work.

2. Optimal Substructure
The solution to a larger problem can be constructed using solutions to smaller subproblems.

Example:

Finding the minimum cost to reach a destination may depend on the minimum costs of reaching previous positions.

3. Choices at Each Step
Many DP problems involve choosing between multiple options.

Examples:

- Take or skip an item.
- Move left or right.
- Buy or sell.
- Include or exclude a character.
- Choose the minimum or maximum result.

Not every problem with choices requires DP. Look for overlapping subproblems and reusable states.
'''