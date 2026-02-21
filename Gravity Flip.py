# Read number of cubes (not really needed)
n = int(input())
# Read cube heights
heights = list(map(int, input().split()))

# Gravity flip → sort cubes
heights.sort()

# Print the result
print(*heights)
