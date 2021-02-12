from collections import*
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    # java에서 toString() 기능, tip: ctrl + o 하면 메서드 오버라이드 하는 창 나옴
    def __str__(self):
        return str(self.data)

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

    def pop(self, data):
        self.root, deletedNode = self._pop(self.root, data)
        return deletedNode
    # 양쪽 자식 있으면 오른쪽 서브트리 중 가장 작은거 삭제해줄거
    def _pop(self, node, data):
        deletedNode = None
        if node is None:
            return node, deletedNode
        if node.data == data:
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
        elif node.data < data:
            node.right, deletedNode = self._pop(node.right, data)
        else:
            node.left, deletedNode = self._pop(node.left, data)
        return node, deletedNode


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
    def preorder(self):
        print("pre-order")
        def _preorder(node):
            if node is None: return
            print(node.data, end=' ')
            _preorder(node.left)
            _preorder(node.right)
        _preorder(self.root)
        print()

    def inorder(self):
        print("in-order")
        def _inorder(node):
            if node is None: return
            _inorder(node.left)
            print(node.data, end=' ')
            _inorder(node.right)
        _inorder(self.root)
        print()

    def postorder(self):
        print("post-order")
        def _postorder(node):
            if node is None: return
            _postorder(node.left)
            _postorder(node.right)
            print(node.data, end=' ')
        _postorder(self.root)
        print()

    # split = True면 층별로 출력
    def levelorder(self, split=False):
        print("level-order")
        def _levelorder(node):
            q = deque([node])
            while q:
                lq = len(q)
                for i in range(lq):
                    node = q.popleft()
                    if node is not None:
                        print(node.data, end=' ')
                        if node.left: q.append(node.left)
                        if node.right: q.append(node.right)
                if split: print()
        _levelorder(self.root)
        print()

if __name__ == "__main__":
    # test
    arr = [3, 1, 5, -32, 61, 223, 41, 53, 62]
    bst = BST()
    for x in arr: bst.push(x)
    bst.levelorder()
    # bst.levelorder(True)
    bst.preorder()
    bst.inorder()
    bst.postorder()
    print(bst.find(1))
    print(bst.find(2))
    
    print(bst.pop(1))
    print(bst.pop(1))


