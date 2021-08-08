# https://www.acmicpc.net/problem/5670
# trie
from sys import*
input = lambda:stdin.readline().rstrip()

class Node:
    def __init__(self):
        self.child = {}
        self.end = 0
class Trie:
    def __init__(self, cnt):
        self.root = Node()
        self.total = 0
        self.cnt = cnt

    def insert(self, params):
        node = self.root
        for param in params:
            if param not in node.child:
                node.child[param] = Node()
            node = node.child[param]
        node.end += 1
    def cal(self):
        for child in self.root.child:
            self._cal(self.root.child[child], 1)
    def _cal(self, node, click):
        node_len = len(node.child)
        self.total += (click * node.end)
        for child in node.child:
            if node.end >= 1 or node_len >= 2:
                self._cal(node.child[child], click + 1)
            else:
                self._cal(node.child[child], click)
while 1:
    try:
        n = int(input())
        trie = Trie(n)
        for i in range(n):
            trie.insert(input())
        trie.cal()
        # print(trie.total, trie.cnt)
        print(f'{trie.total/trie.cnt:.2f}')
    except:
        break