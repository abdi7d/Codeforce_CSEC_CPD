n = int(input())

home_colors = []
away_colors = []

for _ in range(n):
    h, a = map(int, input().split())
    home_colors.append(h)
    away_colors.append(a)

count = 0

for h in home_colors:
    for a in away_colors:
        if h == a:
            count += 1

print(count)
