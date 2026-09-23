# https://codeforces.com/problemset/problem/155/A

action = int(input())
score = input().split()

min_value = int(score[0])
max_value = int(score[0])
amazing = 0

for point in score:
    if int(point) < min_value:
        min_value = int(point)
        amazing += 1
    elif int(point) > max_value:
        max_value = int(point)
        amazing += 1

print(amazing)