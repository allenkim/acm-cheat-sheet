from heapq import heappush, heappop, heapify
if 0 == 0:
	region = 0
	while True:
		region += 1	
		try:
			nvert = int(input())
		except:
			break
		if (nvert == 0):
			break
		nodes = {}
		try:
			for i in range(nvert):
				nodes[i] = []
			for j in range(nvert):
				inp = [int(x) for x in input().split()]
				n = inp[0]
				for k in range(1, len(inp), 2):
					to, w = inp[k], inp[k+1]
					nodes[j].append([to-1, w])
		
			s, goal = [int(x) for x in input().split()]
			s -= 1
			goal -= 1
			INF = 1000000
		except:
			print("")
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
		try:
			time = dijk(s)
			cur = goal
			path = []
			while (not prev[cur] == -1):
				path.append(cur+1)
				cur = prev[cur]
			path.append(cur + 1)
			path.reverse()
			out = str("Case " + str(region) + ": Path =")
			for n in path:
				out += " " + str(n)
			out += "; " + str(time) + " second delay"
			print(out)
		except:
			print(":(")
		input()		
