#https://codeforces.com/problemset/problem/1857/A

t = int(input())

results = []
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    if len(nums) < 2:
        results.append("NO")
        
    if sum(nums) % 2 == 0:
        results.append("YES")
    else:
        results.append("NO")


for result in results:
    print(result)