from math import inf
from queue import Queue

MAX_V = 40

# adj_mat
res = [[0]*MAX_V for _ in range(MAX_V)]
adj_list = [[2,3],[],[1,3,4],[4],[1]]


s = 0 # source
t = 1 # sink

mf = f = 0
p = []

def augment(v, min_edge):
    global res, f, p
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

