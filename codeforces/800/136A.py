# https://codeforces.com/problemset/problem/136/A

person = int(input())
giveto = input().split()
lst = list(giveto)
for i in range(person):
    giveto[i] = int(giveto[i])
    lst[giveto[i]-1] = str(i + 1)
    
lst = " ".join(lst)
print(lst)