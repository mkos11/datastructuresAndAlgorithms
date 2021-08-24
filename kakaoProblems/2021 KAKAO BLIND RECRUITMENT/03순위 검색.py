# https://programmers.co.kr/learn/courses/30/lessons/72412
class Node:
    def __init__(self):
        self.child = {}
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, node, pos, info):
        if pos == len(info) - 1:
            if 'score' not in node.child:
                node.child['score'] = []
            node.child['score'].append(int(info[pos]))
            return
        if info[pos] not in node.child:
            node.child[info[pos]] = Node()
        self.insert(node.child[info[pos]], pos+1, info)
        if '-' not in node.child:
            node.child['-'] = Node()
        self.insert(node.child['-'], pos+1, info)
    def sort_score(self, node):
        if not node: return
        for k, v in node.child.items():
            if k == 'score':
                v.sort()
            else:
                self.sort_score(v)
    def search(self, node, pos, info):
        if pos == len(info) - 1:
            return self.binary_search(node.child['score'], int(info[pos]))
        if info[pos] not in node.child: return 0
        return self.search(node.child[info[pos]], pos+1, info)
    def binary_search(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l + r) // 2
            if arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return len(arr) - l
def solution(info, query):
    trie = Trie()
    for x in info:
        trie.insert(trie.root, 0, list(x.split()))
    trie.sort_score(trie.root)
    answer = []
    for x in query:
        answer.append(trie.search(trie.root, 0, x.replace('and', '').split()))
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))