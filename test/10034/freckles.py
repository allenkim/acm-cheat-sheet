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

def kruskal(V, edge_list):
    edge_list.sort()
    mst_cost = 0
    UF = UFDS(V)
    for w, u, v in edge_list:
        if not UF.is_same_set(u, v):
            mst_cost += w
            UF.union(u, v)
    return mst_cost

TC = int(input())
for _ in range(TC):
    input()
    n = int(input())
    coords = []
    for _ in range(n):
        x, y = [float(i) for i in input().split()]
        coords.append((x,y)) 
    edge_list = []
    for i in range(n):
        for j in range(i+1,n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            d = ((x2-x1)**2 + (y2-y1)**2)**0.5
            edge_list.append((d,i,j))
    mst = kruskal(n, edge_list)
    print("{:0.2f}".format(mst))

