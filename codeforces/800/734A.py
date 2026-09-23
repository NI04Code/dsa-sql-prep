# https://codeforces.com/problemset/problem/734/A

n = int(input())
ad = input()
counta = 0
countd = 0
for i in ad:
    if i == 'A':
        counta += 1
    elif i == 'D':
        countd += 1

if counta > countd:
    print("Anton")
elif counta < countd:
    print("Danik")
else:
    print("Friendship")