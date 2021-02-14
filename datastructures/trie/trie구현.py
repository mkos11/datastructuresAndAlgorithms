# 트라이는 문제 풀면서 적용하기
# https://www.acmicpc.net/problem/5052
from sys import*
input = lambda: stdin.readline().strip()

class Node:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        node = self.root
        for i, char in enumerate(string):
            if i == len(string) - 1:
                # 마지막인데 더 내려갈 수 있음(앞에서 이미 이 경로를 따라간 더 긴게 나왔음, 즉 이 단어는 접두어가 됨)
                if char in node.child: return False
            # 다음 갈 문자 없으면 노드 생성해줌
            if char not in node.child: node.child[char] = Node()
            # 다음 노드로
            node = node.child[char]
            # 아직 이 단어 다 확인 안했는데 end가 있으면 지금 단어보다 더 짧은 접두어가 있음
            if node.end: return False
        node.end = True
        return True

if __name__ == "__main__":
    for tc in range(int(input())):
        trie = Trie()
        isCorrect = True
        for i in range(int(input())):
            string = input()
            # 이미 False면 볼 필요 없음
            if not isCorrect: continue
            if not trie.insert(string): isCorrect = False
        if isCorrect: print("YES")
        else: print("NO")