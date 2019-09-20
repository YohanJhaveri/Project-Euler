"""
=============================================================================================================================================
Problem 7: 10001st prime
---------------------------------------------------------------------------------------------------------------------------------------------

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

=============================================================================================================================================
"""

import math, time

def nth_prime(n):
    primes = [x for x in range(2,200000)]

    for i in range(math.ceil(math.sqrt(200000))):
        for j in range(2, 200000//primes[i]):
            try:               primes.remove(j * primes[i])
            except ValueError: pass

    return primes[n-1]

print(nth_prime(10001))
