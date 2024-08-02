string1 = input().strip()
string2 = input().strip()

string1 = string1.lower()
string2 = string2.lower()
result = 0

if string1 < string2:
    result =  -1
elif string1 > string2:
    result =  1
print(result)