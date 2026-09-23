# https://codeforces.com/problemset/problem/112/A

str1 = input().lower()
str2 = input().lower()
count1 = 0
count2 = 0
for i in range(len(str1)):
    count1 += ord(str1[i])
    count2 += ord(str2[i])
    if ord(str1[i]) < ord(str2[i]):
        print('-1')
        break
    elif ord(str1[i]) > ord(str2[i]):
        print('1')
        break

if count1 == count2:
    print('0')
