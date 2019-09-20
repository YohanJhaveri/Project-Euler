"""
=============================================================================================================================================
Problem 4: Largest palindrome product
---------------------------------------------------------------------------------------------------------------------------------------------

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

=============================================================================================================================================
"""

def palindrome():
    max_palindrome = 0
    for x in range(100,1000):
        for y in range(x,1000): # NOTE: start y from the value of x to prevent symmetric repeats => x * y and y * x
            if str(x*y) == str(x*y)[::-1]: max_palindrome = max(x*y, max_palindrome)
    return max_palindrome

print(palindrome())
