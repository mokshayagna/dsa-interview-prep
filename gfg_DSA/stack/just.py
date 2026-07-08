"""
Build multi-digit numbers

Input

12a3b45

Output
12
3
45
    """
a = "12a3b45"

# numbers = []
# current_num = ""

# for ch in a:
#     if ch.isdigit():
#         current_num += ch
#     else:
#         if current_num != "":
#             numbers.append(current_num)
#             current_num = ""

# if current_num != "":
#     numbers.append(current_num)

# print(numbers)
"""
Remove all digits

Input

ab12cd34

Output

abcd
"""

# a = "ab12cd34"
# l = []
# for ch in a:
#     if ch.isalpha():
#         l.append(ch)
# print("".join(l))

"""
Repeat characters
Input: 3a2b4c

Output: aaabbcccc
    """
# a = "3a2b4c"
# num = 0
# char = ""
# l = []
# for i in a:
#     if i.isdigit():
#         num = int(i)
#     else:
#         char = i
#         while num > 0:
#             l.append(char)
#             num -= 1
# print("".join(l))
    
# n = 10203004
# l = []
# for digit in str(n):
#     if digit != "0":
#         l.append(digit)
#     x = "".join(l)
# sum = 0
# for i in l:
#     sum = sum + int(i)
# print(sum)
# print(x)
# print(type(x))

# print(sum * int(x))
