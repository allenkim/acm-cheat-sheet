sieve_size = 100000
bs = [True] * 100010
primes = []

def sieve():
    bs[0] = bs[1] = False
    for i in range(2, sieve_size+1):
        if bs[i]:
            for j in range(i*i, sieve_size+1, i):
                bs[j] = False
        primes.append(i)

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

sieve()
l = input()
while len(l) > 1:
    n = [int(i) for i in l.split()]
    N = 1
    for i in range(0, len(n), 2):
        N *= n[i]**n[i+1]
    factors = list(reversed(prime_factors(N-1)))
    i = 0
    count = 0
    curr = factors[0]
    freq = []
    for factor in factors:
        if factor == curr:
            count += 1
        else:
            freq.append((curr,count))
            curr = factor
            count = 1
    for f in freq:
        print(f[0], f[1], end=" ")
    print(curr, count)
    l = input()
    

