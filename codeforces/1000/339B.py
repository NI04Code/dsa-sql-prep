# https://codeforces.com/problemset/problem/339/B
input1 = input().split()
input2 = input().split()
pos = 1
counter = 0
max = int(input1[0])

for i in input2:
    if int(i) > pos:
        counter += int(i) - pos
    if int(i) < pos:
        counter += max - pos + int(i)
    
    pos = int(i)

print(counter)