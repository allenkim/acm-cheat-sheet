import math
def extended_euclid(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x, y, d = extended_euclid(b, a % b)
        return (y, x - (a // b) * y, d)

n = int(input())
while n > 0:
    c1, n1 = [int(i) for i in input().split()]
    c2, n2 = [int(i) for i in input().split()]
    x0, y0, d = extended_euclid(n1, n2)
    if n % d != 0:
        print("failed")
    else:
        fac = n // d
        x0 *= fac
        y0 *= fac
        l = math.ceil((-x0)*d / n2)
        u = math.floor(y0*d / n1)
        if l > u:
            print("failed")
        else:
            x1 = x0+(n2//d)*l
            y1 = y0-(n1//d)*l
            x2 = x0+(n2//d)*u
            y2 = y0-(n1//d)*u
            if c1*x1+c2*y1 <= c1*x2+c2*y2:
                print(x1, y1)
            else:
                print(x2, y2)

    n = int(input())

