# https://codeforces.com/problemset/problem/110/A

number = input()
count = 0

for digit in number:
    if digit == '4' or digit == '7':
        count += 1

lst = list(str(count))

lucky = True
for elem in lst:
    if  elem != '4' and elem != '7': 
        lucky = False

if lucky:
    print('YES')
else :
    print('NO')


