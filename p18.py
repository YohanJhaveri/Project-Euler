"""
1:                                 01
2:                             02      03
3:                         04      05      06
4:                     07      08      09      10
5:                 11      12      13      14      15
6:             16      17      18      19      20      21
7:         22      23      24      25      26      27      28


For each node, the index of its two children are calculated as (n + r) and (n + r + 1)
where n is the index of the node and r is the row number of the node

"""
pyramid = [75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,19,1,23,75,3,34,88,2,77,73,7,63,67,99,65,4,28,6,16,70,92,41,41,26,56,83,40,80,70,33,41,48,72,33,47,32,37,16,94,29,53,71,44,65,25,43,91,52,97,51,14,70,11,33,28,77,73,17,78,39,68,17,57,91,71,52,38,17,14,91,43,58,50,27,29,48,63,66,4,68,89,53,67,30,73,16,69,87,40,31,4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

def row(index):
    index += 1
    row = 0
    end = 0
    while index > end:
        row += 1
        end += row
    return row


def largest_path(n):
    if row(n) == row(len(pyramid)-1):
        return pyramid[n]

    else:
        L = largest_path(n + row(n))
        R = largest_path(n + row(n) + 1)

        return max(pyramid[n] + L, pyramid[n] + R)

print(largest_path(0))
