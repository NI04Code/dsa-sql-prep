# https://codeforces.com/problemset/problem/677/A

friend, h = input().split()
friend = int(friend)
h = int(h)
height = input().split()
width = 0
for i in height:
    i = int(i)
    if i > h:
        width += 2
    else:
        width += 1
print(width) 