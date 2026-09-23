# https://codeforces.com/problemset/problem/510/A

n, m = input().split()
n = int(n)
m = int(m)

for i in range(n):
    for j in range(m):
        if (i+1) % 2 == 1:
            print('#', end="")
        elif (i+1) % 4 == 0:
            if j == 0:
                print('#', end="")
            else:
                print('.', end="")
        elif (i+1) % 2 == 0:
            if j == m - 1:
                print('#', end="")
            else:
                print('.', end="")
    print()