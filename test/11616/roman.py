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

while True:
    try:
        s = input()
        if s.isdecimal():
            print(AtoR(int(s)))
        else:
            print(RtoA(s))
    except EOFError:
        break

