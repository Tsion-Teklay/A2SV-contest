matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
 
# Find the position of the number 1
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_distance = abs(i - 2)  # Distance to the middle row (index 2)
            col_distance = abs(j - 2)  # Distance to the middle column (index 2)
            moves_needed = row_distance + col_distance
            print(moves_needed)
            exit()
