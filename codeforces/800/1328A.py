# https://codeforces.com/problemset/problem/1328/A

t = int(input())
lst = [] # list of a and b
for i in range(t):
    a, b = input().split()
    if int(a) < int(b) != 0:
        lst.append(int(b) - int(a))
    elif int(a) % int(b) != 0:
        lst.append(int(b) - (int(a) % int(b)))
    else:
        lst.append(0)


for i in lst:
    print(i)