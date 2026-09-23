# https://codeforces.com/problemset/problem/785/A

count = int(input())
sum = 0
for i in range(count):
    polyhedron = input()
    if polyhedron == "Tetrahedron":
        sum += 4
    elif polyhedron == "Cube":
        sum += 6
    elif polyhedron == "Octahedron":
        sum += 8
    elif polyhedron == "Dodecahedron":
        sum += 12
    elif polyhedron == "Icosahedron":
        sum += 20

print(sum)