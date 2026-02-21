n = int(input())
count = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    # If at least two are sure, count this problem
    if a + b + c >= 2:
        count += 1

print(count)
