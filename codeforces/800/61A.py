# https://codeforces.com/problemset/problem/61/A

num1 = input()
num2 = input()
num3 = ""

for index in range(len(num1)):
    if num1[index] == num2[index]:
        num3 += "0"
    else:
        num3 += "1"

print(num3)