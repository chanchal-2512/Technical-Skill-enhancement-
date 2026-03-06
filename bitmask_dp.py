def min_cost(cost):
    n = len(cost)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        task = bin(mask).count("1")  # number of assigned tasks

        for worker in range(n):
            if not (mask & (1 << worker)):  # worker not assigned
                new_mask = mask | (1 << worker)
                dp[new_mask] = min(dp[new_mask],
                                   dp[mask] + cost[task][worker])

    return dp[(1 << n) - 1]


# Example
cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

print("Minimum Cost:", min_cost(cost))