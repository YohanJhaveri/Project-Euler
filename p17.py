"""
=============================================================================================================================================
Problem 17: Number letter counts
---------------------------------------------------------------------------------------------------------------------------------------------

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

=============================================================================================================================================
"""

num_to_words = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

total = 0
for i in range(1,1001):
    digits = [i%10, (i//10)%10, (i//100)%10, (i//1000)%10]

    if i < 20:
        # print(num_to_words[i])
        total += len(num_to_words[i])

    elif i < 100:
        # print(num_to_words[digits[1]*10] + ' ' + num_to_words[digits[0]])
        total += len(num_to_words[digits[1]*10]) + len(num_to_words[digits[0]])

    elif i < 1000 and i%100 > 20:
        # print(num_to_words[digits[2]] + (' hundred ' if not digits[1] and not digits[0] else ' hundred and ') + num_to_words[digits[1]*10] + ' ' + num_to_words[digits[0]])
        total += len(num_to_words[digits[2]]) + (7 if not digits[1] and not digits[0] else 10) + len(num_to_words[digits[1]*10]) + len(num_to_words[digits[0]])

    elif i < 1000 and i%100 <= 20:
        # print(num_to_words[digits[2]] + (' hundred ' if not i%100 else ' hundred and ') + num_to_words[i%100])
        total += len(num_to_words[digits[2]]) + (7 if not i%100 else 10) + len(num_to_words[i%100])

    elif i == 1000:
        # print('one thousand')
        total += 11

print(total)
