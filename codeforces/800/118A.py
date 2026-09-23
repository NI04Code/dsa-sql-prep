# https://codeforces.com/problemset/problem/118/A
input1 = input()
vowels = ["a", "o", "y", "e", "u", "i"]
lcs = input1.lower()
output = ""
for word in lcs:
    if word not in vowels:
        output += f".{word}"

print(output)