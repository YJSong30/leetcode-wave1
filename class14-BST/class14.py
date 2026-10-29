'''
Binary Search Tree (BST)

- A tree is a data structure made of nodes connected together.
- A Binary Search Tree (BST) is a special kind of tree where every node follows this rule:
- Everything smaller goes to the left. Everything larger goes to the right.

Example: 

        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

      
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def searchBST(root, target):
    current = root

    while current:
        if current.val == target:
            return current

        if target < current.val:
            current = current.left
        else:
            current = current.right

    return None

BST operations depend heavily on height.

Example 1:

1
 \
  2
   \
    3
     \
      4
       \
        5

Search: O(h)
Insert: O(h)
Delete: O(h)

Example 2: Height is small

        4
       / \
      2   6
     / \ / \
    1  3 5  7

Search: O(log n)
Insert: O(log n)
Delete: O(log n)

If you perform inorder traversal on a BST, you get the values in sorted order.
- BST + inorder traversal = sorted order

Recap:

1. Every node has at most 2 children.

2. BST rule:
   left < node < right

3. When searching:
   smaller → left
   larger  → right


   

700) Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        current = root

        while current:
            if current.val == val:
                return current

            if val < current.val:
                current = current.left
            else:
                current = current.right
        
        return None
        

230) Kth Smallest in a BST

Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count = 0
        self.res = None

        def inorder(node):
            if not node:
                return


            inorder(node.left)
            
            # do some work here
            self.count += 1

            if self.count == k:
                self.res = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.res

'''