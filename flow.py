from math import inf
from queue import Queue

MAX_V = 5
res = [[0]*MAX_V for _ in range(MAX_V)]
res[0][2] = 100
res[0][3] = 50
res[2][3] = 50
res[2][4] = 50
res[2][1] = 50
res[3][4] = 100
res[4][1] = 125

adj_list = [[2,3],[],[1,3,4],[4],[1]]
s = 0 # source
t = 1 # sink

mf = f = 0
p = []

def augment(v, min_edge):
    global res, f
    if v == s:
        f = min_edge
        return
    elif p[v] != -1:
        augment(p[v], min(min_edge, res[p[v]][v]))
        res[p[v]][v] -= f
        res[v][p[v]] += f

def edmond_karp():
    global res, mf, f, p
    mf = 0
    while True:
        f = 0
        vis = [False]*MAX_V
        vis[s] = True
        q = Queue()
        q.put(s)
        p = [-1]*MAX_V
        while not q.empty():
            u = q.get()
            if u == t:
                break
            for j in range(len(adj_list[u])):
                v = adj_list[u][j]
                if res[u][v] > 0 and not vis[v]:
                    vis[v] = True
                    q.put(v)
                    p[v] = u
        augment(t, inf)
        if f == 0:
            break
        mf += f
    return mf

