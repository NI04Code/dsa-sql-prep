# https://codeforces.com/problemset/problem/1742/A

n = int(input())

results = []
for i in range(n):
    a, b, c = map(int, input().split())
    
    if a + b == c or a + c == b or b + c == a:
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)