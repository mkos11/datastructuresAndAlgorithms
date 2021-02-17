
# 얘도 BST 먼저 짜고 규칙 찾아보고 다시 짜보기

'''
정의
1. 각 노드 Red or Black
2. 루트노드는 Black
3. 모든 리프노드(NIL 노드)는 Black
4. Red노드의 자식 노드들은 전부 Black(즉, Red노드는 연속되어 등장하지 않음)
5. 모든 노드에 대해 그 노드로부터 자손인 리프노드에 이르는 모든 경로에는 동일한 개수의 Black 노드 존재
'''
# 레드블랙트리 경우의 수 많잖아 이건 그때그때 다시 공부하고 구현하기

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.printTree("", self.root, False)
    def printTree(self, prefix, node, isLeft):
        res = ""
        if node is not None:
            res += f"{prefix}" + ("|-- " if isLeft else "\\-- ") + f"{node.data}\n"
            res += self.printTree(prefix + ("|   " if isLeft else "    "), node.left, True)
            res += self.printTree(prefix + ("|   " if isLeft else "    "), node.right, False)
        return res

    def push(self, data):
        self.root = self._push(self.root, data)
    def _push(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._push(node.left, data)
        else:
            node.right = self._push(node.right, data)
        return node

    def pop(self, data):
        self.root, deletedNode = self._pop(self.root, data)
        return deletedNode
    def _pop(self, node, data):
        deletedNode = None
        if node is None: return node, deletedNode
        if data == node.data:
            deletedNode = node
            if node is None: node = None
            elif node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # node.left or node.right
            else:
                node = node.left or node.right
        elif node.data < data:
            node.left = self._pop(node.left, data)
        else:
            node.right = self._pop(node.right, data)
        return node, deletedNode

if __name__ == "__main__":
    redBlackTree = RedBlackTree()
    data = [i for i in range(1, 16)]
    for x in data: redBlackTree.push(x)
    print(redBlackTree)
    for x in data[:-5]: redBlackTree.pop(x)
    print(redBlackTree)