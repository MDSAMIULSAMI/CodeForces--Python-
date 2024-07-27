loop = int(input())
counter = 0
for i in range(loop):
    x = input()
    if x.count("++X") or x.count("X++"):
        counter = counter + 1
    if x.count("--X") or x.count("X--"):
        counter = counter - 1

print(counter)