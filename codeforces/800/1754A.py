# https://codeforces.com/contest/1754/problem/A

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    inpt = input()
    for chr in inpt:
        if chr == 'Q':
            count += 1
        elif chr == 'A':
            count -= 1
        if count < 0:
            count = 0
    if count == 0:
        print('Yes')
    else:
        print('No')
