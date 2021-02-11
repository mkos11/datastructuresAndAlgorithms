class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None
    def push(self, data):
        self.root = self._push(self.root, data)
    def _push(self, node, data):
        if node is None:
            node = Node(data)
        elif data <= node.data:
            node.left = self._push(node.left, data)
        else:
            node.right = self._push(node.right, data)
        return node
    # pop에서도 find랑 연산 비슷한데 합칠수도 있을듯?, 찾으면 node 리턴하고, 없으면 None 리턴
    def pop(self, data):
        return self._pop(self.find(data))
    # 양쪽 자식 있으면 오른쪽 서브트리 중 가장 작은거 삭제해줄거
    def _pop(self, node, data):
        deletedNode = None
        if node is not None:
            deletedNode = node
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                # 이 부분 주의하기!! 실수함
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                node = None
        return deletedNode


    def find(self, data):
        return self._find(self.root, data)
    def _find(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self._find(node.right, data)
        else:
            return self._find(node.left, data)

    # 순회도 추가하기 (preorder, inoredr, postorder, levelorder)