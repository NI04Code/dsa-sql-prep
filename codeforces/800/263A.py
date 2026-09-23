# https://codeforces.com/problemset/problem/263/A

r1 = input().split()
r2 = input().split()
r3 = input().split()
r4 = input().split()
r5 = input().split()
count = 0
if '1' in r1:
    r3 = r1
    count += 2
elif '1' in r2:
    r3 = r2
    count += 1
elif '1' in r5:
    r3 = r5
    count += 2
elif '1' in r4:
    r3 = r4
    count += 1

if r3[4] == '1' or r3[0] == '1':
    count += 2
elif r3[1] == '1' or r3[3] == '1':
    count += 1


print(count)

