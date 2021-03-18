def solve(preOrder, inOrder):
    if not preOrder: return
    root = preOrder[0]
    # postOrder 출력할거
    pivot = inOrder.index(root)
    solve(preOrder[1:pivot+1], inOrder[:pivot])
    solve(preOrder[pivot+1:], inOrder[pivot+1:])
    print(root,end=' ')
for tc in range(int(input())):
    n = int(input())
    preOrder = list(map(int,input().split()))
    inOrder = list(map(int,input().split()))
    solve(preOrder, inOrder)
    print()
