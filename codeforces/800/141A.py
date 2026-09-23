# https://codeforces.com/problemset/problem/141/A

l1 = input()
l2 = input()
l3 = input()
l4 = l3

for chr in l3:
    if chr in l1:
        l1 = l1.replace(chr, "", 1)
        l4 = l4.replace(chr, "", 1)
    elif chr in l2:
        l2 = l2.replace(chr, "", 1)
        l4 = l4.replace(chr, "", 1)


if (len(l1) + len(l2) + len(l4)) == 0:
    print("YES")
else:
    print("NO")

