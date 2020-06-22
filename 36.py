result = 0
for i in range(1, 1_000_000):
    binary = bin(i)[2:]
    is_palindrome = str(i) == str(i)[::-1] and binary == binary[::-1]
    if is_palindrome:
        result += i
print(result)
        
