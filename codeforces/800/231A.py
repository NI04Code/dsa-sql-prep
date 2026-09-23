# https://codeforces.com/problemset/problem/231/A

problemset = int(input())
implement = 0
for i in range(problemset):
    count = 0
    petya, vasya, tonya = input().split()
    if petya == '1':
        count += 1
    if vasya == '1':
        count += 1
    if tonya == '1':
        count += 1
    if count >= 2:
        implement += 1

print(implement)