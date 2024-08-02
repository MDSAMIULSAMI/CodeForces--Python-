station = int(input())

current_passengers = 0
max_passengers = 0

for i in range(station):
    out, In = map(int, input().split())
    current_passengers = current_passengers - out
    current_passengers = current_passengers + In
    max_passengers = max(max_passengers, current_passengers)

print(max_passengers)