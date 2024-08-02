friend, height = map(int, input().split())

point = [int(item) for item in input().split()]

counter = 0
for i in range(friend):
    if point[i] > height:
        counter = counter + 2
    else:
        counter = counter + 1
print(counter)