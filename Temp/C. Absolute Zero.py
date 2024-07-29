def solve(test_cases):
    results = []
    for case in test_cases:
        n, arr = case
        operations = []
        for _ in range(40):
            max_val = max(arr)
            if max_val == 0:
                break
            operations.append(max_val)
            arr = [abs(a - max_val) for a in arr]
        
        if all(a == 0 for a in arr):
            results.append((len(operations), operations))
        else:
            results.append(-1)
    
    return results
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    test_cases.append((n, arr))
results = solve(test_cases)
for result in results:
    if result == -1:
        print(result)
    else:
        k, ops = result
        print(k)
        print(" ".join(map(str, ops)))
