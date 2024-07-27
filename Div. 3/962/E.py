def solve(s):
    n = len(s)
    mod = 10**9 + 7
    
    # Calculate cumulative sum of 0s and 1s
    count = [0] * (n + 1)
    for i in range(n):
        count[i + 1] = count[i] + (1 if s[i] == '1' else -1)
    
    # Dictionary to store frequencies of cumulative sums
    freq = {0: 1}
    ans = 0
    
    for i in range(n):
        ans = (ans + freq.get(count[i + 1], 0)) % mod
        freq[count[i + 1]] = freq.get(count[i + 1], 0) + 1
    
    return ans

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(solve(s))
