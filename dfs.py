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

def dfs(vertex):
	visited[vertex] = True
	if (visited[goal]):
		return 
	nodes[vertex].sort(key = lambda x: x[1])
	for to in nodes[vertex]:
		if visited[to[0]]:
			continue
		dfs(to[0])

dfs(0)		
print(visited[goal])	
		
	
