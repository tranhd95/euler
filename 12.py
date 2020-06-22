from math import sqrt

sum_of_first_n = lambda n: n*(n-1)/2

def number_of_divisors(n):
    i = 1
    divisors = []
    while i < sqrt(n):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
        i += 1
    return len(set(divisors))

num_of_divisors = 1
triangle_number = 1
i = 1
while num_of_divisors < 500:
    triangle_number = sum_of_first_n(i)
    num_of_divisors = number_of_divisors(triangle_number)
    i += 1
    print(num_of_divisors)
print(triangle_number)

