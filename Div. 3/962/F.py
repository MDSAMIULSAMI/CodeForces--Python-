import heapq

def max_score_after_operations(num_cases, cases):
    results = []
    for case in cases:
        n, k, A, B = case
        max_heap = [-a for a in A]
        heapq.heapify(max_heap)
        
        score = 0
        for _ in range(k):
            if max_heap:
                max_value = -heapq.heappop(max_heap)
                score += max_value

        results.append(score)
    return results

def read_input():
    num_cases = int(input())
    cases = []
    for _ in range(num_cases):
        n, k = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        cases.append((n, k, A, B))
    return num_cases, cases

def main():
    num_cases, cases = read_input()
    results = max_score_after_operations(num_cases, cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
