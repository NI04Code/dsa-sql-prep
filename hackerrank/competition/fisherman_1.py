# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        f = int(input_data[idx+1])
        k = int(input_data[idx+2])
        idx += 3
        
        fishes = []
        for _ in range(n):
            fishes.append(int(input_data[idx]))
            idx += 1
            
        fishes.sort(reverse=True)
        
        max_profit = 0
        current_sum = 0
    
        for i in range(n):
            current_sum += fishes[i]
            cost = ((i + k) // k) * f
            profit = current_sum - cost
            if profit > max_profit:
                max_profit = profit
                
        out.append(str(max_profit))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()