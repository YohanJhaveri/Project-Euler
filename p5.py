"""
=============================================================================================================================================
Problem 5: Smallest multiple
---------------------------------------------------------------------------------------------------------------------------------------------

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

=============================================================================================================================================
"""

from collections import Counter

def prime_factors(n):
    divisor = 2
    factors = []
    while n != 1:
        if n % divisor == 0:
            n //= divisor
            factors.append(divisor)
        else:
            divisor += 1
    return factors

def smallest_multiple():
    factors = {}
    highest = {}
    sum = 1

    for x in range(11, 20):
        factors = Counter(prime_factors(x))
        for y in factors: highest[y] = max(factors[y], highest[y] if y in highest else 0)

    for x in highest:
        sum *= x ** highest[x]

    return sum

print(smallest_multiple())
