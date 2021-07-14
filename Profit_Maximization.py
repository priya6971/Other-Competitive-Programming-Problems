 # You have to travel to different villages to make some profit.In each village, you gain some profit. 
 # But the catch is, from a particular village j, you can only move to a village i 
 # if and only if profit gain of j<i and the profit gain from village i is a 
 # multiple of the profit gain from village j.
 # You have to tell the maximum profit you can gain while traveling.
 # Approach : Dynamic Programming using Memoization 
def max_profit(p, n, memo):
    max = 0
    for i in range(n):
        memo[i] = p[i]
    
    for i in range(1, n):
        for j in range(0, i):
            if p[i]>p[j] and p[i]%p[j]==0 and memo[i] < memo[j]+p[i]:
                memo[i] = memo[j]+p[i]

    for i in range(n):
        if max < memo[i]:
            max = memo[i]
    return max

## Driver code
p = [1, 2, 3, 4, 9, 8]
n = len(p)
memo = [None for i in range(n)]
profit = max_profit(p, n, memo)
print("Maximum Profit is", profit)