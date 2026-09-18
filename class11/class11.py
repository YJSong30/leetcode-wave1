'''
Binary Tree DFS

DFS: Depth-First Search
- goes as deep as possible in one path before coming back

two ways to do dfs on trees:

bottom-up dfs:

def dfs(node):
    if not node:
        return BASE_CASE

    left = dfs(node.left)
    right = dfs(node.right)

    # use left/right to calculate something

    return something

top-down dfs:

def dfs(node, state):
    if not node:
        return

    new_state = ...

    dfs(node.left, new_state)
    dfs(node.right, new_state)


root = [1,2,3,4,5,null,null]

        1
       / \
      2   3
     / \
    4   5

Preorder: Node -> Left -> Right

def dfs(node):
    if not node:
        return

    print(node.val)
    dfs(node.left)
    dfs(node.right)

Result = 1 2 4 5 3

Inorder: Left -> Node -> Right

def dfs(node):
    if not node:
        return

    dfs(node.left)
    print(node.val)
    dfs(node.right)

Result = 4 2 5 1 3

Postorder: Left -> Right -> Node

def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
    print(node.val)

Result = 4 5 2 3 1
'''