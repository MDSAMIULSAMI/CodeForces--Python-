t = int(input())
for i in range(t):
    n,  k = map(int, input().split())
    a = list(map(int, input().strip().split()))[:k]
    counter = 0
    for i in range(1,len(a)):
        if a[i]%2 != 0:
            counter=1
            break
    addition = 0
    if counter == 1:
        for i in range(1,len(a)):
            addition = a[i] + addition
        print(addition)
    if counter == 0:
        for i in range(1,len(a)):
            addition = a[i] + addition
        print(addition+1)