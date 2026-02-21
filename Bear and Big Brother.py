# read initial weights
a, b = map(int, input().split())

years = 0
# simulate year by year until a > b
while a <= b:
    a *= 3
    b *= 2
    years += 1

print(years)
