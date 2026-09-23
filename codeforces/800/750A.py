# https://codeforces.com/problemset/problem/750/A

action = input().split()
problemset = int(action[0])
time = int(action[1])

maxproblem_solved = 0
time_limit = 240 - time
for i in range(problemset):
    time_limit -= (i+1)*5
    if time_limit < 0:
        break
    maxproblem_solved += 1

print(maxproblem_solved)