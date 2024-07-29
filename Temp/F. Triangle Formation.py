def can_form_two_triangles(sticks):
    n = len(sticks)
    if n < 6:
        return "NO"
    sticks.sort()
    for i in range(n - 5):
        for j in range(i + 1, n - 4):
            for k in range(j + 1, n - 3):
                for l in range(k + 1, n - 2):
                    for m in range(l + 1, n - 1):
                        for o in range(m + 1, n):
                            # Form two triangles with these 6 sticks
                            triangle1 = [sticks[i], sticks[j], sticks[k]]
                            triangle2 = [sticks[l], sticks[m], sticks[o]]
                            
                            if (is_triangle(triangle1) and is_triangle(triangle2)):
                                return "YES"
    return "NO"

def is_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a
n, q = map(int, input().split())
stick_lengths = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    subarray = stick_lengths[l-1:r]
    result = can_form_two_triangles(subarray)
    print(result)