# https://codeforces.com/problemset/problem/469/A

level = int(input())
little_x = input().split()
little_y = input().split()
cleared_level = set(little_x[1:] + little_y[1:])

if len(cleared_level) == level:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")