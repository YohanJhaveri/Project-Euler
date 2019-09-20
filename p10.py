"""
=============================================================================================================================================
Problem 10: Summation of primes
---------------------------------------------------------------------------------------------------------------------------------------------

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

=============================================================================================================================================
"""

import math

def sum_of_n_primes(n):
    primes = [x for x in range(2,n)]

    for i in range(math.ceil(math.sqrt(n))):
        for j in range(2, n//primes[i]):
            try:               primes.remove(j * primes[i])
            except ValueError: pass
            
    return sum(primes)

print(sum_of_n_primes(2000000))
