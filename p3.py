"""
=============================================================================================================================================
Problem 3: Largest prime factor
---------------------------------------------------------------------------------------------------------------------------------------------

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

=============================================================================================================================================
"""


def largest_prime_factor(n):
    divisor = 2
    while n != 1:
        if n % divisor == 0: n //= divisor
        else:                divisor += 1
    return divisor

    """

    NOTE:

    =>  divisors will only be prime since the number would have already been divided by
        the prime factors of non-prime divisors before it gets to the non-prime divisor

    =>  the biggest prime factor will be the last factor that divides n evenly, leaving a quotient of 1

    """

n = 600851475143
print(largest_prime_factor(n))
