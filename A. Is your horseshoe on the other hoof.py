# Read four colors
colors = list(map(int, input().split()))

# Count distinct colors
distinct_colors = len(set(colors))

# Minimum to buy = 4 - distinct colors
print(4 - distinct_colors)
