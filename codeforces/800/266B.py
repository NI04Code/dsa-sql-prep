# https://codeforces.com/problemset/problem/266/B
queue_number, sec = input().split()
queue_number = int(queue_number)
sec = int(sec)
queue = input()
queue2 = queue
queue = list(queue)
for i in range(sec):
    queue = queue2
    queue = list(queue)
    queue2 = list(queue2)
    for j in range(queue_number-1):
        if queue[j] == 'B' and queue[j+1] == 'G':
            queue2[j], queue2[j+1] = queue2[j+1], queue2[j]
    queue = "".join(queue)
    queue2 = "".join(queue2)
    
print(queue2)