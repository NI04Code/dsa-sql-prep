# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def soccer_field():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        w = int(input_data[idx])
        h = int(input_data[idx+1])
        n = int(input_data[idx+2])
        idx += 3
            
        circles = []
        for _ in range(n):
            x = int(input_data[idx])
            y = int(input_data[idx+1])
            r = int(input_data[idx+2])
            idx += 3
            circles.append((x, y, r))
            
        circles = list(set(circles))
        n = len(circles)
            
        circles.sort(key=lambda c: c[0] - c[2])
        
        parent = list(range(n + 2))
        TOP = n
        BOTTOM = n + 1
        
        def find(i):
            root = i
            while parent[root] != root:
                root = parent[root]
            curr = i
            while curr != root:
                nxt = parent[curr]
                parent[curr] = root
                curr = nxt
            return root
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                
        blocked = False
        
        for i in range(n):
            xi, yi, ri = circles[i]
            
            if yi + ri >= h:
                union(i, TOP)
            if yi - ri <= 0:
                union(i, BOTTOM)
                
            if find(TOP) == find(BOTTOM):
                blocked = True
                break
                
            right_edge = xi + ri
            for j in range(i + 1, n):
                xj, yj, rj = circles[j]
                
                if xj - rj > right_edge:
                    break  
                    
                if abs(yi - yj) > ri + rj:
                    continue
                    
                if (xi - xj)**2 + (yi - yj)**2 <= (ri + rj)**2:
                    union(i, j)
                    
                    if find(TOP) == find(BOTTOM):
                        blocked = True
                        break
                        
            if blocked:
                break
                
        if blocked:
            out.append("NO")
        else:
            out.append("YES")
            
    print('\n'.join(out))

if __name__ == '__main__':
    soccer_field()
