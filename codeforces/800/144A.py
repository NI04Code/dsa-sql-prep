# https://codeforces.com/problemset/problem/144/A

soldier = int(input())
soldier_height = input().split()
for i in range(len(soldier_height)):
    soldier_height[i] = int(soldier_height[i])
max = soldier_height[0]
min = soldier_height[0]
x = 0
y = 0

counter = 0
for i in range(1, len(soldier_height)):
    if soldier_height[i] > max:
        max = soldier_height[i]
        x = i
while True:
    if soldier_height[0] != max:
        soldier_height[x], soldier_height[x-1] = soldier_height[x-1], soldier_height[x]
        x -= 1
        counter += 1
    else:
        break

for i in range(1, len(soldier_height)):
    if soldier_height[i] <= min:
        min = soldier_height[i]
        y = i
while True:
    if soldier_height[-1] != min:
        soldier_height[y], soldier_height[y+1] = soldier_height[y+1], soldier_height[y]  
        y += 1
        counter += 1
    else:
        break

print(counter)