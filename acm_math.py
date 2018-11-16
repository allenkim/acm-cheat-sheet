import sys
from functools import lru_cache

sys.setrecursionlimit(100000)

#############################
# SOME COMMON MATH FORMULAS #
#############################

@lru_cache(maxsize=None)
def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n-1, k-1) + C(n-1,k)

# Number of distinct binary trees with n vertices
# Number of expressions of n pairs of correctly matched paren
# Number of ways n+1 factors can be parenthesized
# Number of ways a convex polygon of n+2 sides can be triangulated
# Number of monotonic paths along nxn grid which do not pass above diagonal
@lru_cache(maxsize=None)
def cat(n):
    if n == 0:
        return 1
    else:
        return (4*n-2)*Cat(n-1)//(n+1)

# number of permutations such that none appear in original position
@lru_cache(maxsize=None)
def der(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n-1) * (der(n-1) + der(n-2))

# number of permutations of n elements with k disjoint cycles
@lru_cache(maxsize=None)
def stirl1(n, k):
    if n == 0 and k == 0:
        return 1
    elif n == 0 or k == 0:
        return 0
    else:
        return (n-1)*stirl1(n-1, k) + stirl1(n-1, k-1)

# number of ways to partition a set of n objects into k non-empty subsets
@lru_cache(maxsize=None)
def stirl2(n, k):
    if n == 0 and k == 0:
        return 1
    elif n == 0 or k == 0:
        return 0
    else:
        return k*stirl2(n-1, k) + stirl2(n-1, k-1)

# number of permutations of numbers 1 to n in which exactly m elements are greater
# than the previous element (permutations with m "ascents")
@lru_cache(maxsize=None)
def euler1(n, m):
    if m == 0 or m == n-1:
        return 1
    else:
        return (n-m)*euler1(n-1,m-1) + (m+1)*euler1(n-1,m)

# The permutations of the multiset {1, 1, 2, 2, ···, n, n} which have the 
# property that for each k, all the numbers appearing between the two 
# occurrences of k in the permutation are greater than k are counted by the 
# double factorial number (2n−1)!!. The Eulerian number of the second kind 
# counts the number of all such permutations that have exactly m ascents.
@lru_cache(maxsize=None)
def euler2(n, m):
    if n == 0 and m == 0:
        return 1
    elif n == 0:
        return 0
    else:
        return (2*n-m-1)*euler2(n-1, m-1) + (m+1)*euler2(n-1, m)

# Fibonacci Facts
# [[1,1],[1,0]] mat mul for O(log n)
# Zeckendorf's theorem - greedily choose largest fibonacci to represent
# Pisano Period - last one/two/three/four digits repeat 
# with period 60/300/1500/15000 respectively

# Burnside's lemma
# X = set of all possible ways to arrange
# G = set of rotations
# X/G = set of all possible ways to arrange rotationally invariant
# X/G = (1/|G|) sum_{g in G} |X^g|

# 3 colors, 4 sided table
# G = {0, 90, 180, 270}
# (1/4) * (3^4 + 3 + 9 + 3) = 92/4 = 24

# number of rotationally distinct colorings of faces of cube in n colors
# (1/24) * (n**6 + 3*n**4 + 12*n**3 + 8*n**2)

# Cayley's formula
# There are n^{n-2} spanning trees of a complete graph with n labeled vertices

# Degree sequence of graph d1 >= d2 >= ... >= dn
# sum of d_i is even
# sum_{i=1}^k d_i <= k*(k-1) + sum_{i=k+1}^n min(d_i, k)

# Euler's formula for planar graphs
# V - E + F = 2
# F is number of faces in graph

# Moser's circle - number of pieces a circle is divided if n points on 
# circumference are joined by chords with no three internally concurrent
# g(n) = nC4 + nC2 + 1

# Pick's theorem
# I: number of integer points in the polygon
# A: area of polygon
# b: number of integer points on boundary
# A = i + (b//2) - 1

# Number of spanning trees on complete bipartite graph
# K_{n, m} = m^{n-1} * n^{m-1}

# Josephus
# n people and k-th person gets killed
# when k = 2
# n = 1 b_1 b_2 b_3..b_n, answer is b_1 b_2 b_3...b_n 1
# move most significant bit to the back
# people labeled from 0 to n-1
# otherwise, F(n, k) = (F(n-1, k) + k) % n
# F(1, k) = 0

#################
# Cycle finding #
#################

def floyd_cycle(f, x0):
    tortoise = f(x0)
    hare = f(tortoise)
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    # start of cycle
    mu = 0
    hare = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
    # len of cycle
    l = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        l += 1
    return (mu, l)


##################################
# COMMON NUMBER THEORY FUNCTIONS #
##################################
sieve_size = 10000001
bs = [True] * 10000010
primes = []


def sieve():
    bs[0] = bs[1] = False
    for i in range(2, sieve_size+1):
        if bs[i]:
            for j in range(i*i, sieve_size+1, i):
                bs[j] = False
        primes.append(i)

def is_prime(N):
    if N <= sieve_size:
        return bs[N]
    for i in range(len(primes)):
        if N % primes[i] == 0:
            return False
    return True

# Takes a few seconds
def test_prime():
    sieve()
    print(is_prime(2147483647))
    print(is_prime(136117223861))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * (b // gcd(a, b))

# Make sure sieve is called before using
def prime_factors(N):
    factors = []
    PF_idx = 0
    PF = primes[PF_idx]
    while PF*PF <= N:
        while N % PF == 0:
            N //= PF
            factors.append(PF)
        PF_idx += 1
        PF = primes[PF_idx]
    # special case when N is prime
    if N != 1:
        factors.append(N)
    return factors

def test_prime_factors():
    sieve()
    r = prime_factors(2147483647)
    print(r)
    r = prime_factors(136117223861)
    print(r)
    r = prime_factors(142391208960)
    print(r)

def num_pf(N):
    PF_idx = 0
    PF = primes[PF_idx]
    ans = 0
    while PF * PF <= N:
        # check if divisible and incr (for num_diff_pf)
        # also, don't increment inside loop
        while N % PF == 0:
            N //= PF
            ans += 1
            # ans += PF (for sum_pf)
        PF_idx += 1
        PF = primes[PF_idx]
    # special case when N is prime
    if N != 1:
        ans += 1
    return ans

# num_diff_pf and num_sum_pf is trivial change to above
# num_diff_pf for many values can be done through sieve
def num_diff_pf_sieve(N):
    numDiffPF = [0] * N
    for i in range(2, N):
        if numDiffPF[i] == 0:
            for j in range(i, N, i):
                numDiffPF[j] += 1
    return numDiffPF

def num_div(N):
    PF_idx = 0
    PF = primes[PF_idx]
    ans = 1
    while PF * PF <= N:
        power = 0
        while N % PF == 0:
            N //= PF
            power += 1
        ans *= (power + 1)
        PF_idx += 1
        PF = primes[PF_idx]
    if N != 1:
        ans *= 2
    return ans

def sum_div(N):
    PF_idx = 0
    PF = primes[PF_idx]
    ans = 1
    while PF * PF <= N:
        power = 0
        while N % PF == 0:
            N //= PF
            power += 1
        ans *= (PF**(power+1) - 1) // (PF - 1)
        PF_idx += 1
        PF = primes[PF_idx]
    if N != 1:
        ans *= (N*N-1) // (N - 1)
    return ans

def euler_phi(N):
    PF_idx = 0
    PF = primes[PF_idx]
    ans = N
    while PF * PF <= N:
        if N % PF == 0:
            ans -= ans // PF
        while N % PF == 0:
            N /= PF
        PF_idx += 1
        PF = primes[PF_idx]
    if N != 1:
        ans -= ans // N
    return ans

def test_prime_factors():
    sieve()
    print(num_pf(60))
    print(num_div(60))
    print(num_diff_pf_sieve(100))
    print(sum_div(60))
    print(euler_phi(36))

# ax + by = c
# d = gcd(a, b)
# if d | c is not true, no solution

# return (x0, y0, d)
# a*x0 + b*y0 = d
def extended_euclid(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x, y, d = extended_euclid(b, a % b)
        return (y, x - (a // b) * y, d)

# the prime means we have to multiply by c//d to get a solution
# x = x0' + (b//d)*n
# y = y0' - (a//d)*n

########################
# GAUSSIAN ELIMINATION #
########################

# aug is the augmented matrix with size n x n+1
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

# aug = [[1,1,2,9],[2,4,-3,1],[3,6,-5,0]]
# X = [1,2,3]
# print(gauss_elim(aug))

##################
# ROMAN NUMERALS #
##################

def AtoR(A):
    cvt = {}
    cvt[1000] = "M"
    cvt[900] = "CM"
    cvt[500] = "D"
    cvt[400] = "CD"
    cvt[100] = "C"
    cvt[90] = "XC"
    cvt[50] = "L"
    cvt[40] = "XL"
    cvt[10] = "X"
    cvt[9] = "IX"
    cvt[5] = "V"
    cvt[4] = "IV"
    cvt[1] = "I"
    s = ""
    keys = sorted(cvt.keys(),reverse=True)
    for i in keys:
        while A >= i:
            s += cvt[i]
            A -= i
    return s

def RtoA(R):
    cvt = {}
    cvt['I'] = 1
    cvt['V'] = 5
    cvt['X'] = 10
    cvt['L'] = 50
    cvt['C'] = 100
    cvt['D'] = 500
    cvt['M'] = 1000
    
    value = 0
    i = 0
    while i < len(R):
        if i+1 < len(R) and cvt[R[i]] < cvt[R[i+1]]:
            value += cvt[R[i+1]] - cvt[R[i]]
            i += 1
        else:
            value += cvt[R[i]]
        i += 1
    return value

