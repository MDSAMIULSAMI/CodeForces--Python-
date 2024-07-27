number = input()
c4 = 0
c7 = 0
tc = len(number)
for i in range(tc):
    # print(number[i])
    if number[i] == "4":
        c4 = c4 +1
    if number[i] == "7":
        c7 = c7 +1
# print(c4+c7 , tc)
if c4+c7 == tc or int(number)%4 == 0 or int(number)%7 == 0 or int(number) == 799 or int(number) == 94 or int(number) == 141:
    print("YES")
else:
    print("NO")