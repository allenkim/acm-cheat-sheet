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

def count_letters(n):
    freq = {}
    freq['i'] = 0
    freq['v'] = 0
    freq['x'] = 0
    freq['l'] = 0
    freq['c'] = 0
    for i in range(n+1):
        s = AtoR(i).lower()
        for c in s:
            freq[c] += 1
    return freq

n = int(input())
while n > 0:
    freq = count_letters(n)
    print("{}: {} i, {} v, {} x, {} l, {} c".format(n,freq['i'],freq['v'],freq['x'],freq['l'],freq['c']))
    n = int(input())

