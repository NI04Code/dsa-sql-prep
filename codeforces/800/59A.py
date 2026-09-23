# https://codeforces.com/problemset/problem/59/A

word = input()
count_upper = 0
count_lower = 0

for char in word:
    if 64 < ord(char) < 91:
        count_upper += 1
    elif 96 < ord(char) < 123:
        count_lower += 1

if count_upper > count_lower:
    print(word.upper())
else:
    print(word.lower())
