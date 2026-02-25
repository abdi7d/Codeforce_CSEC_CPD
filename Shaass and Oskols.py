n = int(input())
birds = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  # convert to 0-based index
    
    left = y - 1
    right = birds[x] - y
    
    if x - 1 >= 0:
        birds[x - 1] += left
        
    if x + 1 < n:
        birds[x + 1] += right
        
    birds[x] = 0

for b in birds:
    print(b)
