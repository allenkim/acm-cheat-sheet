n, cap = [int(x) for x in input().split()]

items = []
for i in range(n):
	items.append([int(x) for x in input().split()]) #weight, value

dp = [[0 for x in range(cap+1)] for x in range(n+1)] #dp[n][capacity]

for i in range(n+1):
	for c in range(cap+1):
		if (i == 0 or c == 0): #fill in base cases
			dp[i][c] = 0
		elif items[i-1][0] <= c: #can carry 
			# best here is the max of
			# value of nth item + best value with n-1 items and c less capacity
			# or n-1 items (rejecting the item)
			dp[i][c] = max(items[i-1][1] + dp[i-1][c-items[i-1][0]], dp[i-1][c])
		else:
			dp[i][c] = dp[i-1][c]
print(dp[i][c])

