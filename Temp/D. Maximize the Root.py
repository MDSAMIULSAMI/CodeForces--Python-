def main():
    from collections import defaultdict
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        p = list(map(int, input().strip().split()))
        tree = defaultdict(list)
        for child in range(2, n + 1):
            parent = p[child - 2]
            tree[parent].append(child)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = a[i]
        def dfs(node):
            if node not in tree:
                return dp[node]
            total = dp[node]
            for child in tree[node]:
                total += dfs(child)
            if len(tree[node]) > 0:
                dp[node] = total // len(tree[node])
            
            return total
        dfs(1)
        results.append(dp[1])
    for result in results:
        print(result)
if __name__ == "__main__":
    main()