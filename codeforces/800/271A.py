# https://codeforces.com/problemset/problem/271/A

year = input()
valid = True
while valid:
    year = int(year)
    year += 1
    year = str(year)
    st = set(year)
    if len(st) == 4:
        print(year)
        valid = False