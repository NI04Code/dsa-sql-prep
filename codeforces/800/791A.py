# https://codeforces.com/problemset/problem/791/A

limak, bob = input().split()
limak = int(limak)
bob = int(bob)

years = 0
while limak <= bob:
    limak *= 3
    bob *= 2
    years += 1

print(years)