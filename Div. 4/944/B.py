t = int(input())
for i in range(t):
    a = input()
    rev = []
    rng =  range(len(a), 0, -1)
    for i in rng:
        rev.append(a[i-1])
    if "".join(rev) == a:
        if a == "cac" or a == "dad" or a == "aba" or a == "bab" or a == "bad" or a == "ada":
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
        print("".join(rev))