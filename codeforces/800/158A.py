# https://codeforces.com/problemset/problem/158/A

n, k = input().split()
n = int(n)
k = int(k)
lst = input().split()
lst = [int(number) for number in lst]
count = 0
if n >= k:
    for i in lst[:n]:
        if i >= lst[k-1] and i > 0:
            count += 1

    print(count)


