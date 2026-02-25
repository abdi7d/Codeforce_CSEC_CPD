# Read input
s = input().strip()
t = input().strip()

pos = 0  # pointer to current stone (0-based index)

for char in t:
    if pos < len(s) and char == s[pos]:
        pos += 1

# Output final position (1-based index)
print(pos + 1)
