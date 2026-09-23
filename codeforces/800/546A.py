# https://codeforces.com/problemset/problem/546/A

price, money, amount = input().split()
price = int(price)
money = int(money)
amount = int(amount)
total_price = 0
for i in range(1,amount+1):
    total = price*i
    total_price += total
if total_price - money >= 0:
    print(total_price-money)
else:
    print(0)