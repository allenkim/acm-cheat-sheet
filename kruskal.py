from collections import defaultdict
class UFDS:
	def __init__(self, vertices):
		self.V = vertices
		self.rank = defaultdict(list)
		self.parent = defaultdict(list)
		for i in range(vertices):
			self.rank[i] = 1
			self.parent[i] = i

	def find(self, i):
		if not self.parent[i] == i:
			self.parent[i] = self.find(self.parent[i])
		return self.parent[i]
	
	def union(self, a, b):
		if (self.isSameSet(a, b)):
			return	
		x = self.find(a)
		y = self.find(b)
		if (self.rank[x] > self.rank[y]):
			self.parent[y] = x
		else:
			self.parent[x] = y
			if (self.rank[x] == self.rank[y]):
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

