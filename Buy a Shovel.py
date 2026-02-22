n, k = map(int, input().split())

for x in range(1, 11):
    if (n * x) % k == 0 or (n * x) % 10 == 0:
        print(x)
        break
