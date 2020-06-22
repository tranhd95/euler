i = 2
f_1 = 1
f_2 = 1
digits = 1

while digits < 1000:
    nxt = f_1 + f_2
    f_1 = f_2
    f_2 = nxt
    i += 1
    digits = len(list(str(nxt)))
print(i)