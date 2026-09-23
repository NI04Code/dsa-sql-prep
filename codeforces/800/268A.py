# https://codeforces.com/problemset/problem/268/A

loop = int(input())
lst1 = []
lst2 = []

for i in range(loop):
    a, b = input().split()
    lst1.append(a)
    lst2.append(b)

sum = 0
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if i == j:
            continue
        if lst1[i] == lst2[j]:
            sum += 1

print(sum)
