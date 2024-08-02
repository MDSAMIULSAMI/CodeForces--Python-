def maximize_bananas(t, test_cases):
    results = []
    for i in range(t):
        a, b, c = test_cases[i]
        nums = [a, b, c]
        nums.sort()
        for _ in range(5):
            nums[0] += 1
            nums.sort()
        
        results.append(nums[0] * nums[1] * nums[2])
    return results
    
if __name__ == "__main__":
    t = int(input())
    test_cases = []
    
    for _ in range(t):
        a, b, c = map(int, input().split())
        test_cases.append((a, b, c))
    
    results = maximize_bananas(t, test_cases)
    
    for result in results:
        print(result)
