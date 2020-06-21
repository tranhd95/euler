is_palindrome = lambda x: x == x[::-1]
palindromes = []
def foo():
    for i in range(1000, 99, -1):
        for j in range(1000, 99, -1):
            candidate = i*j
            if is_palindrome(str(candidate)):
                palindromes.append(candidate)
    return max(palindromes)

print(foo())

        