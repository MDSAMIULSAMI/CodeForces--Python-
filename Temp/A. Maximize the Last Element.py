def max_remaining_element(arr):
    if len(arr) == 1:
        return arr[0]
    
    while len(arr) > 1:
        max_sum = float('-inf')
        max_index = 0
        # Find the pair with the maximum sum
        for i in range(len(arr) - 1):
            current_sum = arr[i] + arr[i + 1]
            if current_sum > max_sum:
                max_sum = current_sum
                max_index = i
        
        # Remove the pair with the maximum sum
        arr = arr[:max_index] + [max_sum] + arr[max_index + 2:]
    
    return arr[0]

def main():
    # Read the number of test cases
    t = int(input())
    
    results = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        result = max_remaining_element(arr)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
