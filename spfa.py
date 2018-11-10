from queue import *
nvert, nedge, goal = [int(x) for x in input().split()]

INF = 10000000

nodes = {}
dist = {}
for i in range(nvert):
	nodes[i] = []
	dist[i] = INF

for _ in range(nedge):
	fr, to, w= [int(x) for x in input().split()]
	nodes[fr].append([to, w])
	nodes[to].append([fr, w])


def spfa(start):
	dist[start] = 0
	q = Queue()
	q.put(start)
	while (not q.empty()):
		u = q.get()	
		for v in nodes[u]:
			if (dist[u] + v[1] < dist[v[0]]): #s -> u -> v shorted than s -> v
				dist[v[0]] = dist[u] + v[1]
				#if v[0] not in q:
				q.put(v[0])
spfa(0)	
print(dist[goal])	
		
	
