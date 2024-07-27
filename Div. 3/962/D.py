def count_triplets(n, x):
    count = 0
    for c in range(1, n // (x - 2) + 1):
        a_b_max = (n // c)
        if a_b_max >= x - c:
            count += (a_b_max - (x - c) + 1) * (x - c)
    return count

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        result = count_triplets(n, x)
        print(result)
