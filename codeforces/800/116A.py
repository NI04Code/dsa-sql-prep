# https://codeforces.com/problemset/problem/116/A

n = int(input())
trum_rn = 0
trum_capacity = 0

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    trum_rn -= a
    trum_rn += b
    if trum_capacity < trum_rn:
        trum_capacity = trum_rn

print(trum_capacity)