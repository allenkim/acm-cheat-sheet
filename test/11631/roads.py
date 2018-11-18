class UFDS:
    def __init__(self, N):
        self.rank = [0] * N
        self.p = list(range(N))

    def find(self, i):
        if not self.p[i] == i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, a, b):
        if not self.is_same_set(a, b):
            x = self.find(a)
            y = self.find(b)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

    def is_same_set(self, a, b):
        return self.find(a) == self.find(b)	

# V: number of vertices
# edge_list: [(w,u,v),...] (weight, start, end)
def kruskal(V, edge_list):
    edge_list.sort()
    mst_cost = 0
    UF = UFDS(V)
    for w, u, v in edge_list:
        if not UF.is_same_set(u, v):
            mst_cost += w
            UF.union(u, v)
    return mst_cost

V, E = [int(i) for i in input().split()]
while V != 0:
    edge_list = []
    total = 0
    for _ in range(E):
        x, y, z = [int(i) for i in input().split()]
        total += z
        edge_list.append((z,x,y))
    mst = kruskal(V, edge_list)
    print(total-mst)
    V, E = [int(i) for i in input().split()]

