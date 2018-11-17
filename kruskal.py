#sort edges

#create disjoint set of indices

#for each edge, attempt to add if not same same

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

	def isSameSet(self, a, b):
		return self.find(a) == self.find(b)	


