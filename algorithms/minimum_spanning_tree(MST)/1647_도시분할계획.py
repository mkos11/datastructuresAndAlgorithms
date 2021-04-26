from sys import*
input = stdin.readline

def find(u):
    if parent[u] == u: return u
    parent[u] = find(parent[u])
    return parent[u]
def union(u, v):
    u = find(u)
    v = find(v)
    if u == v: return False
    parent[u] = v
    return True
INF = int(1e9)
V, E = map(int,input().split())
adj = []*V
res = 0
for i in range(E):
    u, v, w = map(int,input().split())
    u-=1; v-=1;
    adj.append((u, v, w))
adj.sort(key=lambda x: x[2])
parent = [i for i in range(V)]
connected = 0
MAX = 0
res = 0
for u, v, w in adj:
    if connected == V-1: break
    if(union(u, v)):
        connected+=1
        res += w
        MAX = max(MAX, w)
print(res-MAX)
