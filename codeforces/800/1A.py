# https://codeforces.com/problemset/problem/1/A
x = input().split()
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])
ceiling1 = 0
ceiling2 = 0
if (x1 % x3 != 0):
    ceiling1 = 1
if (x2 % x3 != 0):
    ceiling2 = 1
answer = ((x1 // x3) + ceiling1) * ((x2 // x3) + ceiling2)
print(answer)
