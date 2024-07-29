from collections import deque, defaultdict

def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = set()
    for p in range(2, n + 1):
        if is_prime[p]:
            prime_numbers.add(p)
    return prime_numbers

def solve(test_cases, max_n):
    max_xor = 2 * max_n
    prime_numbers = sieve(max_xor)
    results = []
    
    for n in test_cases:
        if n == 1:
            results.append((1, [1]))
            continue
        
        graph = defaultdict(list)
        for u in range(1, n + 1):
            for v in range(u + 1, n + 1):
                if (u ^ v) in prime_numbers:
                    graph[u].append(v)
                    graph[v].append(u)
        
        color = [0] * (n + 1)
        available_colors = [0] * (n + 1)
        
        for node in range(1, n + 1):
            if color[node] == 0:
                queue = deque([node])
                while queue:
                    u = queue.popleft()
                    forbidden = set()
                    for v in graph[u]:
                        if color[v] != 0:
                            forbidden.add(color[v])
                        if color[v] == 0:
                            queue.append(v)
                    for c in range(1, n + 1):
                        if c not in forbidden:
                            color[u] = c
                            break
        
        k = max(color)
        results.append((k, color[1:]))
    return results
t = int(input().strip())
test_cases = []
max_n = 0
for _ in range(t):
    n = int(input().strip())
    test_cases.append(n)
    max_n = max(max_n, n)
results = solve(test_cases, max_n)
for result in results:
    k, colors = result
    print(k)
    print(" ".join(map(str, colors)))
