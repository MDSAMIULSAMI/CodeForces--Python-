m, n, a = input().split()

x = 0
y = 0 

if int(m)%int(a) == 0:
    x = int(m)/int(a)
else:
    x = int(m)/int(a) + 1
if int(n)%int(a) == 0:
    y = int(n)/int(a)
else:
    y = int(n)/int(a) + 1

print(int(x)*int(y))