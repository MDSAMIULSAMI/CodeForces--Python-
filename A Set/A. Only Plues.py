t = int(input())

for i in range(t):
    a , b , c = input().split()
    if int(a) < 10 and int(b) < 10 and int(c) < 10:
        a = int(a) + 3
        b = int(b) + 2
        c = int(c)
        print(a*b*c)
    else:
        if int(a) == 10:
            b = int(b) + 5
        if int(b) == 10:
            c = int(c) + 5
        if int(c) == 10:
            c = int(c)
        print(int(a)*int(b)*int(c))