"""
=============================================================================================================================================
Problem 21: Amicable numbers
---------------------------------------------------------------------------------------------------------------------------------------------

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

=============================================================================================================================================
"""

import math

def divisor_sum(n):
    sum_of_divisors = 1
    for x in range(2, math.ceil(math.sqrt(n))):
        if n % x == 0:
            sum_of_divisors += x
            sum_of_divisors += n / x
    return sum_of_divisors

def amicable_numbers(n):
    sum_of_divisors = {x: divisor_sum(x) for x in range(n)}

    amicable_numbers = set()
    for x in range(n):
        if(sum_of_divisors[x] < n and sum_of_divisors[sum_of_divisors[x]] == x and sum_of_divisors[x] != x):
            amicable_numbers.add(x)

    return sum(amicable_numbers)

print(amicable_numbers(10000))
