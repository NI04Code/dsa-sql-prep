#Tribonnaci is a sequence where f(n) = f(n-1) + f(n-2) + f(n-3)
def tribonnaci(n):
    dp = [0 for _ in range(n+3)] # n+3 in order not get index oob when user query n=0 or n=1 (we only use n index)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

n = int(input())
print(tribonnaci(n))