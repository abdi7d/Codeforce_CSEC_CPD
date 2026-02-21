# Read the 5x5 matrix
matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the position of '1'
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            # Calculate moves to center (2,2 in 0-indexed)
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
            exit()
