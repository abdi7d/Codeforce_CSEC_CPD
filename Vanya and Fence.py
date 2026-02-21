# Read n and h from input
n, h = map(int, input().split())
# Read the list of heights
heights = list(map(int, input().split()))

width = 0
for height in heights:
    # If height is more than h, friend bends -> width + 2
    if height > h:
        width += 2
    else:
        width += 1

print(width)
