t =  int(input())
for i in range(t):
    s = input()
    if s.startswith("YES") or s.startswith("YEs") or s.startswith("Yes") or s.startswith("YeS") or s.startswith("YeS") or s.startswith("yES") or s.startswith("yes") or s.startswith("yeS") or s.startswith("yEs"):
        print("YES")
    else:
        print("NO")