from collections import Counter

s = "abcac"
n = 28

new = s * 5 + "abc"
new2 = []

length = len(s)
multiple = n // length
remainder = n % length

new = s.count('a') * multiple + s[:remainder].count('a')
print(new)

# newString = s*multiple + s[:loop]
# print(newString)

# count = Counter(newString)
# print(count.get('a'))

# print(count)
# # print(multiple)
# # print(loop)
# print(new)