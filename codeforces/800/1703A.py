# https://codeforces.com/problemset/problem/1703/A
x = int(input())
lst = []
for i in range(x):
    a = input()
    lst.append(a.lower())

for i in lst:
    if i == "yes":
        print("YES")
    else:
        print("NO")