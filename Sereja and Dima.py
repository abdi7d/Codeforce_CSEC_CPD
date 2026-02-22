n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1

sereja_score = 0
dima_score = 0

turn = 0  # 0 = Sereja, 1 = Dima

while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1

    if turn == 0:
        sereja_score += chosen
    else:
        dima_score += chosen

    turn = 1 - turn  # switch turn

print(sereja_score, dima_score)
