# https://codeforces.com/problemset/problem/1352/A

x = int(input())
lstoutput1 = []
lstoutput2 = []

for i in range(x):
    y = int(input())
    counter = 0
    multiplier = 1
    lst = []
    while y != 0:
        modulo_10 = y % 10
        if (modulo_10 != 0):
            lst.append(modulo_10 * multiplier)
            y = y - modulo_10 
            counter += 1
        y //= 10
        multiplier *= 10

    lstoutput1.append(counter)
    lstoutput2.append(lst)

for i in range(len(lstoutput1)):
    print(lstoutput1[i])
    print(" ".join(map(str, lstoutput2[i])))
