def collatz(n):
    length = 1
    while n > 1:
        isEven = n % 2 == 0
        if isEven:
            n = n/2
        else:
            n = 3*n + 1
        length += 1
    return length

mxm_length = -1
mxm_start_number = 1
for i in range(1_000_000):
    chain_length = collatz(i)
    if chain_length > mxm_length:
        mxm_length = chain_length
        mxm_start_number = i

print(mxm_start_number, mxm_length)

