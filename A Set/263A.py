matrix = []
for _ in range(5):
    row = list(map(int, input().strip().split()))
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_index = i
            col_index = j
            break
moves = abs(row_index - 2) + abs(col_index - 2)
print(moves)
