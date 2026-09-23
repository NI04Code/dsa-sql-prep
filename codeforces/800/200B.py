# https://codeforces.com/problemset/problem/200/B

drinks = int(input())
percentage = input().split()
total_percent = 0
for percent in percentage:
    total_percent += int(percent)

mean = total_percent/drinks
print(mean)