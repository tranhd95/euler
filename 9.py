from math import sqrt

def pyth():
    for a in range(1,1000):
        for b in range(1,1000):
            if a >= b:
                continue
            c = sqrt(a**2 + b**2)
            if b >= c:
                continue
            print(a, b, c)
            if a + b + c == 1000:
                return a,b,c
print(pyth())