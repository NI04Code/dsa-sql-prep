# https://codeforces.com/problemset/problem/486/A

n = int(input())
if n%2 == 1:
    print(int((n+1)/2 * (-1)))
else:
    print(int(n/2))

