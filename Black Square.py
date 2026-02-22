# Read calories for buttons 1,2,3,4
calories = list(map(int, input().split()))

# Read the string of button presses
s = input().strip()

total = 0

for ch in s:
    total += calories[int(ch) - 1]

print(total)
