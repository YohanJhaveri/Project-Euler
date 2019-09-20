"""
=============================================================================================================================================
Problem 24: Lexographic permutations
---------------------------------------------------------------------------------------------------------------------------------------------


=============================================================================================================================================
"""

def permute(A):
    print(A)
    if len(A) == 1:
        return [A]
    permutations = []
    for index, number in enumerate(A):
        other_permutations = permute(A[:index] + A[index+1:])
        permutations += map(lambda permutation: [number] + permutation, other_permutations)
    return permutations

for i in permute([0,1,2,3]):
    print(i)
