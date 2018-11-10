from queue import *

nvert, nedge, goal = [int(x) for x in input().split()]

nodes = {}
for i in range(nvert):
	nodes[i] = []

for _ in range(nedge):
	fr, to, w= [int(x) for x in input().split()]
	nodes[fr].append([to, w])
	nodes[to].append([fr, w])

visited = {}
for i in range(nvert):
	visited[i] = False


def bfs(start):
	q = Queue()
	q.put(start)
	while (not q.empty()):
		vertex = q.get()
		visited[vertex] = True
		if (visited[goal]):
			return 
		nodes[vertex].sort(key = lambda x: x[1])
		for to in nodes[vertex]:
			if visited[to[0]]:
				continue
			q.put(to[0])
	
bfs(0)	
print(visited[goal])	
		
	
