"""
=============================================================================================================================================
Problem 25: 100-digit Fibonacci number
---------------------------------------------------------------------------------------------------------------------------------------------


=============================================================================================================================================
"""

def fibonacci(n):
    f1 = 1
    f2 = 1
    f3 = 2
    index = 3
    while len(str(f3)) < n:
        f1 = f2
        f2 = f3
        f3 = f2 + f1
        index += 1

    return index

print(fibonacci(1000))
