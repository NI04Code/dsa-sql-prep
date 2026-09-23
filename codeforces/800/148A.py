# https://codeforces.com/problemset/problem/148/A

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

damaged_dragon = 0
for i in range(1, d+1):
    if i % l == 0:
        damaged_dragon += 1
    elif i % m == 0:
        damaged_dragon += 1
    elif i % n == 0:
        damaged_dragon += 1
    elif i % k == 0:
        damaged_dragon += 1

print(damaged_dragon)
