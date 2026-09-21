s = "cadbzabcd"

# max_length = 0
# for i in range(len(s)):
#   my_set = set()

#   for j in range(i, len(s)):
#     if s[j] in my_set:
#       break

#     max_length = max(max_length, j - i + 1 )
#     my_set.add(s[j])

# print(max_length)


my_dict = {}
left = 0
right = 0
max_len = 0

while right < len(s):
  if s[right] in my_dict:
    left = max(left, my_dict[s[right]] + 1)

  max_len = max(max_len, right - left + 1 )
  my_dict[s[right]] = right
  right += 1

print(max_len)   