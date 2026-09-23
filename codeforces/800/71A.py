# https://codeforces.com/problemset/problem/71/A
 
loop = int(input())

for i in range(loop):
    word = input()
    if len(word) <= 10:
        print(word)
    else :
        number = str(len(word) - 2)
        word = word[0] + number + word[len(word)-1]
        print(word)

