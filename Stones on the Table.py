n = int(input())
stones = input().strip()

removals = 0

for i in range(1, n):
    if stones[i] == stones[i - 1]:
        removals += 1

print(removals)
