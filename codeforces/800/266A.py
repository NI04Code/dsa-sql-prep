# https://codeforces.com/problemset/problem/266/A

stones_number = int(input())
stone = input()
remove = 0
for i in range(stones_number-1):
    if stone[i] == stone[i+1]:
        remove += 1

print(remove)