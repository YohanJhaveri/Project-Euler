"""
=============================================================================================================================================
Problem 9: Special Pythagorean triplet
---------------------------------------------------------------------------------------------------------------------------------------------

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

=============================================================================================================================================
"""

import math

def pythagorean_triplet_sum(n):
    for x in range(1,1000):
        for y in range(x,1000):
            z = math.sqrt((x * x) + (y * y))
            if x + y + z == n:
                return int(x * y * z)
    return False

print(pythagorean_triplet_sum(1000))
