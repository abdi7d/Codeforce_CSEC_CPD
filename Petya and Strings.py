# Read the two strings
s1 = input().strip()
s2 = input().strip()

# Convert both to lowercase for case-insensitive comparison
s1_lower = s1.lower()
s2_lower = s2.lower()

# Compare
if s1_lower < s2_lower:
    print(-1)
elif s1_lower > s2_lower:
    print(1)
else:
    print(0)
