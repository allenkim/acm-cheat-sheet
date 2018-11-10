def gauss_elim(aug):
    N = len(aug)
    X = [0]*N
    for j in range(N-1):
        l = j
        for i in range(j+1, N):
            if abs(aug[i][j]) > abs(aug[l][j]):
                l = i
        for k in range(j, N+1):
            t = aug[j][k]
            aug[j][k] = aug[l][k]
            aug[l][k] = t
        for i in range(j+1, N):
            for k in range(N, j-1, -1):
                aug[i][k] -= aug[j][k] * aug[i][j] / aug[j][j]
    for j in range(N-1, -1, -1):
        t = 0
        for k in range(j+1, N):
            t += aug[j][k] * X[k]
        X[j] = (aug[j][N] - t) / aug[j][j]
    return X

def eval(coeff, x):
    ans = coeff[-1]
    for val in reversed(coeff[:-1]):
        ans *= x
        ans += val
    return ans

N = int(input())
for _ in range(N):
    vals = []
    for _ in range(1500):
        vals.append(int(input()))
    aug = []
    for i in range(7):
        i += 1
        aug.append([1,i,i**2,i**3,i**4,i**5,i**6,vals[i-1]])
    X = gauss_elim(aug)
    X = [round(x) for x in X]
    done = False
    for val in X:
        if val < 0 or val > 1000:
            print("This is a smart sequence!")
            done = True
            break
    if done:
        input()
        continue
    for i in range(1500):
        if eval(X, i+1) != vals[i]:
            print("This is a smart sequence!")
            done = True
            break
    if not done:
        for val in X[:-1]:
            print(val, end=" ")
        print(X[-1], end="")
        print()
    input()

