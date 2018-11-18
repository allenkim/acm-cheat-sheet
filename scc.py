dfs_num = []
dfs_low = []
S = []
visited = []
dfsNumberCounter = 0
numSCC = 0
V = 12
adj_list = [
    [1],
    [2],
    [3],
    [1],
    [5],
    [6],
    [4],
    [8,11],
    [9],
    [7,10],
    [7],
    [10]
]

def tarjanSCC(u):
    global dfs_num, dfs_low, S, visited, dfsNumberCounter, numSCC
    dfs_low[u] = dfs_num[u] = dfsNumberCounter
    dfsNumberCounter += 1
    S.append(u)
    visited[u] = 1
    for j in range(len(adj_list[u])):
        v = adj_list[u][j]
        if not dfs_num[v]:
            tarjanSCC(v)
        if visited[v]:
            dfs_low[u] = min(dfs_low[u], dfs_low[v])
    if dfs_low[u] == dfs_num[u]:
        numSCC += 1
        print("SCC {}".format(numSCC))
        while True:
            v = S.pop()
            visited[v] = 0
            print(" {}".format(v))
            if u == v:
                break
        print()

dfs_num = [False] * V
dfs_low = [0] * V
visited = [0] * V
dfsNumberCounter = numSCC = 0
for i in range(V):
    if not dfs_num[i]:
        tarjanSCC(i)

