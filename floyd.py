nvert, nedge, goal = [int(x) for x in input().split()]

INF = 10000000

nodes = {}
for i in range(nvert):
	nodes[i] = {}
	for j in range(nvert):
		nodes[i][j] = INF


for _ in range(nedge):
	fr, to, w = [int(x) for x in input().split()]
	nodes[fr][to] = w
	nodes[to][fr] = w

for k in range(nvert):
	for i in range(nvert):
		for j in range(nvert):
			nodes[i][j] = min(nodes[i][j], nodes[i][k] + nodes[k][j])
print(nodes[0][goal])	
		
	
