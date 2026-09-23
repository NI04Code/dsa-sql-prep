# https://codeforces.com/problemset/problem/41/A

a = input()
b = input()

if b == a[::-1]:
    print('YES')
else:
    print('NO')