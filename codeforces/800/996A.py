# https://codeforces.com/problemset/problem/996/A

money = int(input())
count = 0
while money > 0:
    if money >= 100:
        count += money // 100
        money = money % 100
    elif money >= 20:
        count += money // 20
        money = money % 20
    elif money >= 10:
        count += money // 10
        money = money % 10
    elif money >= 5:
        count += money // 5
        money = money % 5
    else:
        count += money
        money = 0

print(count)