"""
=============================================================================================================================================
Problem 14: Longest Collatz Sequence
---------------------------------------------------------------------------------------------------------------------------------------------

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest sequence?

=============================================================================================================================================
"""

def longest_collatz_sequence(n):
    longest_number = 1
    longest_sequence = 1
    for i in range(1,n):
        number = i
        sequence = 1 # 1 is for the intial i itself
        while i != 1:
            i = i//2 if i%2==0 else 3*i + 1
            sequence += 1
        if sequence > longest_sequence:
            longest_sequence = sequence
            longest_number = number
    return longest_number

print(longest_collatz_sequence(1000000))
