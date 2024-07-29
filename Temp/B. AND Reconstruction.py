def reconstruct_and(t, test_cases):
    results = []
    for test_case in test_cases:
        n, b = test_case
        a = [0] * n
        
        # Initialize the first element
        a[0] = b[0]
        for i in range(1, n-1):
            a[i] = b[i-1] | b[i]
        # Initialize the last element
        a[n-1] = b[n-2]
        
        # Validate if the constructed array a is valid
        valid = True
        for i in range(n-1):
            if (a[i] & a[i+1]) != b[i]:
                valid = False
                break
        
        if valid:
            results.append(a)
        else:
            results.append([-1])
    
    return results

# Function to read input and execute the solution
def main():
    t = int(input())
    test_cases = []
    
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        test_cases.append((n, b))
    
    results = reconstruct_and(t, test_cases)
    for result in results:
        if result == [-1]:
            print(-1)
        else:
            print(" ".join(map(str, result)))

# Example usage
main()
