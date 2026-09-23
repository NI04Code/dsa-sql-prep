# https://codeforces.com/problemset/problem/705/A

layer = int(input())
hulk_expression = ""
for i in range(1,layer+1):
    if i == layer and i % 2 == 1:
        hulk_expression += "I hate it "
    elif i == layer and i % 2 == 0:
        hulk_expression += "I love it "
    elif i % 2 == 1:
        hulk_expression += "I hate that "
    else:
        hulk_expression += "I love that "

print(hulk_expression)