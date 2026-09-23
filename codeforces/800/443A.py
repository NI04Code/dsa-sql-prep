# https://codeforces.com/problemset/problem/148/A

letter_set = input()
letter_set = letter_set.strip("}{")
lst = letter_set.split(", ")

if lst[0] == '':
    print(0)
else:
    print(len(set(lst)))