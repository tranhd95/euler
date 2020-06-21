"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

multiplies_of_three = set(range(0, 1000, 3))
multiplies_of_five = set(range(0, 1000, 5))
multiplies = multiplies_of_three.union(multiplies_of_five)

print(sum(multiplies))