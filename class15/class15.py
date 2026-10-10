'''
Trie

A Trie is a tree used to store words/prefixes.
Instead of each node storing a whole number like a BST:
    5
   / \
  3   8

each Trie node usually represents a character.
If we insert:
- cat
- car
- dog

we get roughly:
root
├── c
│   └── a
│       ├── t   ← "cat"
│       └── r   ← "car"
└── d
    └── o
        └── g   ← "dog"

Notice how "cat" and "car" share the prefix: "ca"

That's the entire reason Tries are useful.

class TrieNode:
    def __init__(self):
        self.children = {}
        # self.is_end = False
        self.words = []

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True

trie = Trie()

trie.insert("apple")

print(trie.search("apple"))     # True
print(trie.search("app"))       # False
print(trie.startsWith("app"))   # True

trie.insert("app")
print(trie.search("app"))       # True
        

1268. Search Suggestions System

You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return 
the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, product):
        node = self.root

        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            if len(node.words) < 3:
                node.words.append(product)

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        trie = Trie()
        res = []

        for product in products:
            trie.insert(product)
        
        node = trie.root
        flag = True

        for char in searchWord:
            if flag and char in node.children:
                node = node.children[char]
                res.append(node.words)
            else:
                flag = False
                res.append([])

        return res

'''