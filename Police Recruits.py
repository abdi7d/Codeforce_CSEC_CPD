n = int(input())
events = list(map(int, input().split()))

officers = 0
untreated = 0

for event in events:
    if event > 0:
        officers += event
    else:  # event == -1
        if officers > 0:
            officers -= 1
        else:
            untreated += 1

print(untreated)
