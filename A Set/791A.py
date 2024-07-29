a , b = map(int, input().split())

years = 0
if a == 1 and b == 1:
    years = 1
else:
    while a < b:
        a = 3*a
        b = 2*b
        years = years + 1
if a == b and a != 1:
    print(years+1)
else:
    print(years)