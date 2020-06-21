a = 1
b = 2
result = 2
while a + b < 4_000_000:
    nxt = a + b
    if nxt % 2 == 0:
        result += nxt
    a = b
    b = nxt
print(result)
