a = int(input())
b = int(input())
c = int(input())

part0 = a+b+c
part1 = a+b*c
part2 = a*(b+c)
part3 = a*b*c
part4 = (a+b)*c
result = 0

if result < part0:
    result = part0
if result < part1:
    result = part1
if result < part2:
    result = part2
if result < part3:
    result = part3
if result < part4:
    result = part4
print(result)