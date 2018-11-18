from queue import *
n = int(input())
nodes = [[]]*n
inc = [0]*n
total = 0

nedge = int(input())
for i in range(nedge):
	to, fr = [int(x) for x in input().split()]
	inc[fr] += 1
	nodes[to].append([fr])

ans = []
q = Queue()
for i in range(n):
	if inc[i] == 0:
		q.put(i)
while(not q.empty()):
	u = q.get()
	inc[u] -= 1
	ans.append(u)
	for n in nodes[u]:
		inc[n[0]] -= 1
		if inc[n[0]] == 0:
			q.put(n[0])
print(ans)	
	
