class Node:
    def __init__(self, num):
        self.num = num
        self.childs = []
def solve(node):
    res = 0
    if not node.childs: return 1
    for child in node.childs:
        if child == removeNode:
            if len(node.childs)==1: res += 1
        else: res += solve(nodes[child])
    return res
n = int(input())
inp = list(map(int,input().split()))
nodes = {}
for i in range(n):
    nodes[i] = Node(i)

for i in range(n):
    if inp[i] == -1: root = nodes[i]
    else: nodes[inp[i]].childs.append(i)
removeNode = int(input())
if removeNode == root.num: print(0)
else: print(solve(root))
