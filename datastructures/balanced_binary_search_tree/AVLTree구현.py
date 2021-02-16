# 왼쪽, 오른쪽 서브트리 높이 차 1이하
# LL, RR, LR, RL 그려보면 됨
# 함수 insert, delete, search, leftRotate, rightRotate 만들면 될듯?

# 삽입: 기냥 이진탐색트리대로 삽입하고 불균형 생기면 해소 시켜줌!
# 삭제: 기냥 이진탐색트리대로 삭제하고 불균형 생기면 해소 시켜줌!
# 회전: 그려보면 됨

# 일단 BST 구현하고, 추가되어야 할것들 생각해보기(leftRotation, rightRotation 연산이랑 node에 높이?)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.height = 0
    def __str__(self):
        return f"data: {self.data}, height: {self.height}"
class AVLTree:
    def __init__(self):
        self.root = None

    def push(self, data):
        self.root = self._push(self, self.root, data)
    def _push(self, node, data):
        if node is None: return Node(data)
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
        # 찾음
        if data == node.data:
            deletedNode = node
            # 양쪽 다 있으면 오른쪽 서브트리 제일 왼쪽 원소 가져올거
            if node.left and node.right:
                parent, child = node, node.right
                # 조건 정하고 다시 while문 처리
                while child.left is not None:
                    parent, child = child, child.left
                if node != parent:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 왼쪽만 있음
            elif node.left:
                node = node.left
            # 오른쪽만 있음
            elif node.right:
                node = node.right
            # 자식 없음
            else:
                node = None
        elif data < node.data:
            node.left = self._pop(node.left, data)
        else:
            node.right = self._pop(node.right, data)
        return node, deletedNode