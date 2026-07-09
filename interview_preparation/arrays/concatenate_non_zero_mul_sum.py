"""
Example 1:

Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]

Output: [12340, 4, 9]

Explanation:

s[0..7] = "10203004"
x = 1234
sum = 1 + 2 + 3 + 4 = 10
Therefore, answer is 1234 * 10 = 12340.
s[1..3] = "020"
x = 2
sum = 2
Therefore, the answer is 2 * 2 = 4.
s[4..6] = "300"
x = 3
sum = 3
Therefore, the answer is 3 * 3 = 9.
"""
s = "10203004"
queries = [[0,7], [1,3], [4,6]]

output = []

for left, right in queries:
    substring = s[left:right+1]

    digits = []

    for digit in substring:
        if digit != '0':
            digits.append(digit)

    x = int(''.join(digits))
    sum_of_digits = sum(int(d) for d in digits)

    output.append(x * sum_of_digits)

print(output)