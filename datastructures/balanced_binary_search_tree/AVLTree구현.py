# 왼쪽, 오른쪽 서브트리 높이 차 1이하
# LL, RR, LR, RL 그려보면 됨
# 함수 push, pop, rotate(LL, RR, LR, RL), balance, getHeight, getDifference

# 삽입: 기냥 이진탐색트리대로 삽입하고 불균형 생기면 해소 시켜줌!
# 삭제: 기냥 이진탐색트리대로 삭제하고 불균형 생기면 해소 시켜줌!
# 회전: 그려보면 됨

# 일단 BST 구현하고, 추가되어야 할것들 생각해보기(node높이)
# 생각보다 구현이 좀 더 빡세네 ??ㅎㅎ;;

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.height = 1
    # 노드 str 오버라이딩 해놓으니까 디버깅 할때도 좋더라
    def __str__(self):
        return f"data: {self.data}, height: {self.height}"

class AVLTree:
    def __init__(self):
        self.root = None

    # 이진트리 콘솔에 이쁘게 출력되도록
    def __str__(self):
        return self.printTree("", self.root, False)
    def printTree(self, prefix, node, isLeft):
        res = ""
        if node is not None:
            res += f"{prefix}" + ("|-- " if isLeft else "\\-- ") + f"{node.data}\n"
            res += self.printTree(prefix + ("|   " if isLeft else "    "), node.left, True)
            res += self.printTree(prefix + ("|   " if isLeft else "    "), node.right, False)
        return res

    def getHeight(self, node):
        if node is None: return 0
        return node.height

    def getDifference(self, node):
        if node is None: return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def balance(self, node):
        diff = self.getDifference(node)
        if diff >= 2:
            # LL
            if self.getDifference(node.left) >= 1:
                node = self.rotateLL(node)
            # LR
            else:
                node = self.rotateLR(node)
        elif diff <= -2:
            # RR
            if self.getDifference(node.right) <= -1:
                node = self.rotateRR(node)
            # RL
            else:
                node = self.rotateRL(node)
        # left or right None이면? => 그래서 getHeight() 만들어서 None은 0으로 처리
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        return node

    def roatateLL(self, node):
        leftNode = node.left
        node.left = leftNode.right
        leftNode.right = node
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        return leftNode

    def rotateRR(self, node):
        rightNode = node.right
        node.right = rightNode.left
        rightNode.left = node
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        return rightNode

    def rotateLR(self, node):
        leftNode = node.left
        node.left = self.rotateRR(leftNode)
        return self.roatateLL(node)

    def rotateRL(self, node):
        rightNode = node.right
        node.right = self.roatateLL(rightNode)
        return self.rotateRR(node)

    def push(self, data):
        self.root = self._push(self.root, data)
    def _push(self, node, data):
        if node is None: return Node(data)
        if data < node.data:
            node.left = self._push(node.left, data)
        else:
            node.right = self._push(node.right, data)
        return self.balance(node)

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
                child.left = node.left
                if node != parent:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 왼쪽 or 오른쪽
            elif node.left or node.right:
                node = node.left or node.right
            # 자식 없음
            else:
                node = None
                return node, deletedNode
        elif data < node.data:
            node.left, deletedNode = self._pop(node.left, data)
        else:
            node.right, deletedNode = self._pop(node.right, data)
        return self.balance(node), deletedNode

if __name__ == "__main__":
    avlTree = AVLTree()
    data = [i for i in range(1, 16)]
    for x in data:
        avlTree.push(x)
    print(avlTree)
    for x in data[:5]:
        avlTree.pop(x)
    print(avlTree)