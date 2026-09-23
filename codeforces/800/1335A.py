# https://codeforces.com/problemset/problem/1335/A

t = int(input())
lst_input = []

for i in range(t):
    x = int(input())
    lst_input.append(x)

for i in lst_input:
    if i % 2 == 0:
        i -= 1
    a = i//2 + 1
    print(i-a)
    

