n = input()
string = input()
counter = 0
for i in range(len(string)):
    store =  string[i]
    if store == "A":
        counter = counter + 1

if counter*2 > len(string):
    print("Anton")
elif counter*2 < len(string):
    print("Danik")
else:
    print("Friendship")