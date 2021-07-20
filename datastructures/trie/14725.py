# https://www.acmicpc.net/problem/14725
# Trie
from sys import*
input = lambda: stdin.readline().rstrip()
class Node:
    def __init__(self):
        self.child = {}
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, params):
        node = self.root
        for param in params:
            if param not in node.child:
                node.child[param] = Node()
            node = node.child[param]

    def draw(self, node, depth):
        for child in sorted(node.child):
            print(('-W-'*depth) + child)
            self.draw(node.child[child], depth+1)

n = int(input())
trie = Trie()
for i in range(n):
    trie.insert(list(map(str, input().split()))[1:])
trie.draw(trie.root, 0)
