# https://codeforces.com/problemset/problem/282/A

loop = int(input())
x = 0
for i in range(loop):
    operator = input()
    if '+' in operator:
        x += 1
    elif '-' in operator:
        x -= 1

print(x)
