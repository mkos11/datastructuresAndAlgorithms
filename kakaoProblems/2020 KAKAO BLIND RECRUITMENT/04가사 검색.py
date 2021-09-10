# https://programmers.co.kr/learn/courses/30/lessons/60060
# 일단 생각 나는대로 풀었는데 메모이제이션 더 간단한 방법 있을듯?
# 트라이 재귀로 구현 했다가 하나 시간초과 나길래 반복문으로 바꿔줬더니 통과됨..
from sys import *
setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()
class Node:
    def __init__(self):
        self.child = {}
        self.cnt = {}
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        self._insert(self.root, word, len(word))
    def _insert(self, node, word, word_size):
        for w in word:
            if word_size not in node.cnt: node.cnt[word_size] = 1
            else: node.cnt[word_size] += 1
            if w not in node.child: node.child[w] = Node()
            node = node.child[w]
    def search(self, query):
        return self._search(self.root, 0, query, len(query))
    def _search(self, node, pos, query, query_size):
        if query[pos] == '?':
            return node.cnt[query_size] if query_size in node.cnt else 0
        return self._search(node.child[query[pos]], pos+1, query, query_size) if query[pos] in node.child else 0

def solution(words, queries):
    trie = Trie()
    reverse_trie = Trie()
    for word in words:
        trie.insert(word)
        reverse_trie.insert(word[::-1])
    answer = []
    for query in queries:
        if query[0] != '?': answer.append(trie.search(query))
        else: answer.append(reverse_trie.search(query[::-1]))
    return answer
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))