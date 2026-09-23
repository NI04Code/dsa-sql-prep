# https://codeforces.com/problemset/problem/977/A

a, b = input().split()
a = int(a)
b = int(b)
for i in range(b):
    if a % 10 == 0:
        a //= 10
    else:
        a -= 1

print(a)