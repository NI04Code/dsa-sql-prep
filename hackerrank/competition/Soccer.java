import java.io.*;
import java.util.*;

public class Soccer {
    
    static class Circle implements Comparable<Circle> {
        long x, y, r;
        public Circle(long x, long y, long r) {
            this.x = x;
            this.y = y;
            this.r = r;
        }
        
        @Override
        public int compareTo(Circle other) {
            // Sort strictly by left bounding edge (X - R)
            long thisLeft = this.x - this.r;
            long otherLeft = other.x - other.r;
            if (thisLeft != otherLeft) {
                return Long.compare(thisLeft, otherLeft);
            }
            if (this.x != other.x) return Long.compare(this.x, other.x);
            if (this.y != other.y) return Long.compare(this.y, other.y);
            return Long.compare(this.r, other.r);
        }
        
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Circle c = (Circle) o;
            return x == c.x && y == c.y && r == c.r;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(x, y, r);
        }
    }

    static int[] parent;
    
    // Iterative path-compression find (O(1) amortized, no recursion limit risk)
    static int find(int i) {
        int root = i;
        while (parent[root] != root) {
            root = parent[root];
        }
        int curr = i;
        while (curr != root) {
            int nxt = parent[curr];
            parent[curr] = root;
            curr = nxt;
        }
        return root;
    }
    
    static void union(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) {
            parent[rootI] = rootJ;
        }
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    String line = br.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner fs = new FastScanner();
        String tStr = fs.next();
        if (tStr == null) return;
        int t = Integer.parseInt(tStr);
        
        StringBuilder out = new StringBuilder();
        
        for (int tc = 0; tc < t; tc++) {
            fs.nextLong(); // w (unused)
            long h = fs.nextLong();
            int n = fs.nextInt();
            
            if (n == 0) {
                out.append("YES\n");
                continue;
            }
            
            // Optimization: Remove identical circles using a HashSet
            HashSet<Circle> uniqueCircles = new HashSet<>();
            for (int i = 0; i < n; i++) {
                long x = fs.nextLong();
                long y = fs.nextLong();
                long r = fs.nextLong();
                uniqueCircles.add(new Circle(x, y, r));
            }
            
            n = uniqueCircles.size();
            Circle[] circles = new Circle[n];
            int idx = 0;
            for (Circle c : uniqueCircles) {
                circles[idx++] = c;
            }
            
            Arrays.sort(circles);
            
            parent = new int[n + 2];
            for (int i = 0; i < n + 2; i++) {
                parent[i] = i;
            }
            
            int TOP = n;
            int BOTTOM = n + 1;
            boolean blocked = false;
            
            for (int i = 0; i < n; i++) {
                long xi = circles[i].x;
                long yi = circles[i].y;
                long ri = circles[i].r;
                
                // Connect to boundaries if touching
                if (yi + ri >= h) {
                    union(i, TOP);
                }
                if (yi - ri <= 0) {
                    union(i, BOTTOM);
                }
                
                // Early exit if the current circle completes the wall
                if (find(TOP) == find(BOTTOM)) {
                    blocked = true;
                    break;
                }
                
                long rightEdge = xi + ri;
                for (int j = i + 1; j < n; j++) {
                    long xj = circles[j].x;
                    long yj = circles[j].y;
                    long rj = circles[j].r;
                    
                    // Sweep-line: check forward until the next circle's left edge
                    // is completely past our right edge.
                    if (xj - rj > rightEdge) {
                        break;
                    }
                    
                    // Fast Y bounding box check
                    if (Math.abs(yi - yj) > ri + rj) {
                        continue;
                    }
                    
                    // Exact geometric intersection check
                    long dx = xi - xj;
                    long dy = yi - yj;
                    long rSum = ri + rj;
                    
                    if (dx * dx + dy * dy <= rSum * rSum) {
                        union(i, j);
                        if (find(TOP) == find(BOTTOM)) {
                            blocked = true;
                            break;
                        }
                    }
                }
                
                if (blocked) {
                    break;
                }
            }
            
            if (blocked) {
                out.append("NO\n");
            } else {
                out.append("YES\n");
            }
        }
        
        System.out.print(out.toString());
    }
}
