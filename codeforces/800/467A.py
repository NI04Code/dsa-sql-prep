# https://codeforces.com/problemset/problem/467/A
room = int(input())
count = 0
for i in range(room):
    p, q = input().split()
    p = int(p)
    q = int(q)
    if q - p >= 2:
        count += 1
        
print(count)
