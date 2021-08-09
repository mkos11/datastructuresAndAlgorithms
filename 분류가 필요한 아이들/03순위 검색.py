# https://programmers.co.kr/learn/courses/30/lessons/72412
class Node:
    def __init__(self):
        self.child = {}
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, node, pos, info):
        if info[pos] not in node.child:
            node.child[info[pos]] = Node()
        self.insert(node.child[info[pos]], pos+1, info)
        if '-' not in node.child:
            node.child['-'] = Node()
        self.insert(node.child['-'], pos+1, info)
#       pos basecase 잡아서 숫자 처리해줘야함, 나중에 숫자 배열 정렬도 생각해줘야함
def solution(info, query):
    trie = Trie()
    for x in info:
        trie.insert(trie.root, 0, list(x.split()))
    answer = []
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))