word = input().strip()

current_position = 0  # starting at 'a'
total_steps = 0

for ch in word:
    target_position = ord(ch) - ord('a')
    
    diff = abs(target_position - current_position)
    steps = min(diff, 26 - diff)
    
    total_steps += steps
    current_position = target_position

print(total_steps)
