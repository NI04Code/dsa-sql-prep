# https://codeforces.com/problemset/problem/520/A

a = int(input())
b = input()
b = b.lower()
c = True
alphabet = "qwertyuiopasdfghjklzxcvbnm"

for char in alphabet:
    if char not in b:
        c = False
        break
            


if c == False:
    print("NO")
else:
    print("YES")

