from heapq import heappush, heappop, heapify

nvert, nedge, goal = [int(x) for x in input().split()]

nodes = {}
for i in range(nvert):
	nodes[i] = []

for _ in range(nedge):
	fr, to, w= [int(x) for x in input().split()]
	nodes[fr].append([to, w])
	nodes[to].append([fr, w])

INF = 10000000

distance = {}
prev = {}
unvisited = []

def dijk(start):
	
	distance[start] = 0
	
	for i in range(nvert):
		if (not i == start):
	 		distance[i] = INF
		prev[i] = -1
		
		heappush(unvisited, (distance[i], i))
		
	while(unvisited):
		v = heappop(unvisited) #dist, node
		for n in nodes[v[1]]: #neighbor n (to, pathWeight)
			alt = v[0] + n[1] #start to cur + cur to next
			if (alt < distance[n[0]]): #shorter path, update
				distance[n[0]] = alt 
				prev[n[0]] = v[1]
				for i in range(len(unvisited)):
					if (unvisited[i][1] == n[0]):
						unvisited[i] = (alt, n[0])
						break
				heapify(unvisited)
	return distance[goal]

print(dijk(0))
cur = goal
path = []
while (not prev[cur] == -1):
	path.append(cur)
	cur = prev[cur]
path.append(cur)
path.reverse()
print(path)
	
	
	
	
	
