# https://codeforces.com/problemset/problem/427/A

action = int(input())
number = input().split()
police_counter = 0
crime_counter = 0

for i in number:
    if int(i) > 0:
        police_counter += int(i)
    elif int(i) == -1 and police_counter > 0:
        police_counter -= 1
    else:
        crime_counter += 1


print(crime_counter)

