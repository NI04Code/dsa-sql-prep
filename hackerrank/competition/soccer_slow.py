# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

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
        top_nodes = []
        bottom_nodes = []
        
        for i in range(n):
            x = int(input_data[idx])
            y = int(input_data[idx+1])
            r = int(input_data[idx+2])
            idx += 3
            circles.append((x, y, r))
            
            # Check if this circle intersects the Top or Bottom boundaries
            if y + r >= h:
                top_nodes.append(i)
            if y - r <= 0:
                bottom_nodes.append(i)
                
        # Fast path if a single circle touches both Top and Bottom
        blocked = False
        bottom_set = set(bottom_nodes)
        
        for node in top_nodes:
            if node in bottom_set:
                blocked = True
                break
                
        if blocked:
            out.append("NO")
            continue
            
        # BFS to find if there is a connected component of circles 
        # that connects the Top boundary to the Bottom boundary.
        visited = set(top_nodes)
        queue = deque(top_nodes)
        
        while queue and not blocked:
            curr = queue.popleft()
            cx, cy, cr = circles[curr]
            
            for nxt in range(n):
                if nxt not in visited:
                    nx, ny, nr = circles[nxt]
                    # Check if circles intersect
                    if (cx - nx)**2 + (cy - ny)**2 <= (cr + nr)**2:
                        if nxt in bottom_set:
                            blocked = True
                            break
                        visited.add(nxt)
                        queue.append(nxt)
                        
        if blocked:
            out.append("NO")
        else:
            out.append("YES")
            
    print('\n'.join(out))

if __name__ == '__main__':
    soccer_field()
