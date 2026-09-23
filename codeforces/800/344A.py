# https://codeforces.com/problemset/problem/344/A

amount = int(input())
count = 1
lst = []
for i in range(amount):
    magnetpole = input()
    lst.append(magnetpole)

if len(lst) == 1:
    pass
else:
    for i in range(1, len(lst)):
        if lst[i-1] != lst[i]:
            count += 1

print(count)