string1 = input()
string2 = input()
rever = ""
for i in range(1,len(string1)+1):
    rever = rever + string1[-i]

if rever == string2:
    print("YES")
else:
    print("NO")